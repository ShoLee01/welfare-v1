import os
import time
from groq import Groq
from pydantic import ValidationError
from models import (
    PatientData,
    MedicalRecommendation
)

SYSTEM_PROMPT = """Eres un sistema experto médico que debe:
1. Analizar síntomas, edad, género e historial médico
2. Priorizar síntomas con mayor riesgo vital
3. Asignar UNA sola especialidad de la lista, solo en caso los síntomas presentados representan con Gravedad 5 asignarás 'Medicina General'
4. Calcular gravedad (1-5) según urgencia
5. Respuesta ESTRICTAMENTE en formato JSON válido

**Reglas:**
- Especialidad PRINCIPAL basada en síntomas dominantes
- Considerar factores de riesgo (edad, historial familiar)
- Síntomas cardíacos = prioridad máxima (ejemplo)
- Gravedad 5 = emergencia vital inmediata
- Validar estructura ANTES de responder
- Si los síntomas son claramente algo muy urgente asignar 'Medicina General' y no PRIORIZAR OTRA ESPECIALIDAD
- Si los síntoma son muy variados y no tienen una relacion directa se mandará a Medicina General o Medicina Familiar según el caso

**Ejemplo válido:**
{"specialty": "Medicina General", "severity": 5}



Nota: 
1. No me des una respuesta diferente y no digas nada más en la respuesta 
2. Si consideras que lo que se describe es una area muy especifica que no se encuetra en las Especialidades válidas asignarás Medicina General por defecto
3. Si los síntomas presentados representan con Gravedad 5 asignarás Medicina General
"""

SYSTEM_PROMPT_NEW = """Eres un clasificador médico de emergencias que DEBES seguir estas reglas en orden jerárquico:

1. Prioridad absoluta de Gravedad 5:

Si existe CUALQUIER síntoma de:
hipotensión persistente, alteración de conciencia, dolor torácico aplastante,
dificultad respiratoria severa, hemorragia incontrolable o saturación O₂ < 90%

Especialidad: Medicina General y Gravedad: 5 (sin excepciones)

2. Análisis de contexto crítico:

- Si hay múltiples síntomas sistémicos (ej: fiebre + ictericia + hipotensión)

- Si existe descompensación de comorbilidades (diabetes/Hipertensión/ETC)

- Si el paciente tiene antecedentes relacionados + síntomas agudos

Priorizar Medicina General sobre especialidades específicas

3. Asignación de especialidad (SOLO si Gravedad < 5):

Analizar síntoma dominante usando tabla:
Cardiovascular: dolor torácico, palpitaciones, síncope  
Neurológico: convulsiones, parálisis, cefalea explosiva  
Digestivo: hematoquecia, vómito persistente, ascitis  
[etc...]  

Si no hay coincidencia clara o síntomas multisistémicos se asigna Medicina Familiar (sin excepciones)

4. Validación final OBLIGATORIA:

- Verificar que Gravedad 5 anula cualquier lógica de especialidad

Asegurar JSON válido:
{"specialty": "[valor]", "severity": [1-5]}  

Ejemplo CORRECTO (caso grave):
{"specialty": "Medicina General", "severity": 5}  

Ejemplo INCORRECTO:
{"specialty": "Gastroenterología", "severity": 4}  // ¡Violó regla 1! 
"""

SPECIALTIES = [
    "Medicina General",
    "Pediatría",
    "Geriatría",
    "Medicina Familiar",
    "Ginecología",
    "Obstetricia",
    "Psicología",
    "Psiquiatría",
    "Dermatología",
    "Cardiología",
    "Gastroenterología",
    "Endocrinología",
    "Traumatología",
    "Urología",
    "Neurología",
    "Neumología",
    "Oftalmología",
    "Otorrinolaringología",
    "Nutrición",
    "Fisioterapia",
    "Terapia del Lenguaje",
    "Terapia Ocupacional"
]

ERROR_RESPONSE = {
    "error": "Nuestro sistema de triaje no está disponible. Por seguridad, contacte directamente a un servicio médico de emergencia."
}

async def get_medical_recommendation(patient_data: PatientData) -> MedicalRecommendation:

    user_input = f"""Datos del paciente:
- Síntomas: {patient_data.symptoms}
- Edad: {patient_data.age}
- Género: {patient_data.gender}
- Historial médico: {', '.join(patient_data.medical_history) or 'Ninguno'}
- Historial familiar: {', '.join(patient_data.family_history) or 'Ninguno'}"""

    max_retries = 2
    attempt = 0

    groq = Groq(
        api_key=os.getenv("GROQ_KEY"),
    )

    while attempt <= max_retries:
        try:
            chat_completion = groq.chat.completions.create(
                messages=[
                    {
                        "role": "system",
                        "content": SYSTEM_PROMPT_NEW + f"\n\nEspecialidades válidas:\n{SPECIALTIES}"
                    },
                    {
                        "role": "user",
                        "content": user_input
                    }
                ],
                model="llama3-70b-8192",
                temperature=0,
                response_format={"type": "json_object"},
                stream=False
            )
            
            json_response = chat_completion.choices[0].message.content
            validated = MedicalRecommendation.model_validate_json(json_response)
            
            # Validación adicional de dominio médico
            if validated.specialty not in SPECIALTIES:
                raise ValidationError(f"Especialidad inválida: {validated.specialty}")
                
            if not 1 <= validated.severity <= 5:
                raise ValidationError("Nivel de gravedad fuera de rango")
            
            return validated

        except ValidationError as ve:
            print(ve)
            if attempt >= max_retries:
                return MedicalRecommendation(**ERROR_RESPONSE)
            attempt += 1
            time.sleep(0.5)  # Backoff corto

        except Exception as e:
            print(e)
            return MedicalRecommendation(**ERROR_RESPONSE)

    return MedicalRecommendation(**ERROR_RESPONSE)