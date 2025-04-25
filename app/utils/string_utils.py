import os
import time
from groq import Groq
from pydantic import ValidationError
from models import (
    PatientData,
    MedicalRecommendation
)

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
    SYSTEM_PROMPT = """Eres un sistema experto médico que debe:
1. Analizar síntomas, edad, género e historial médico
2. Priorizar síntomas con mayor riesgo vital
3. Asignar UNA sola especialidad de la lista
4. Calcular gravedad (1-5) según urgencia
5. Respuesta ESTRICTAMENTE en formato JSON válido

**Reglas:**
- Especialidad PRINCIPAL basada en síntomas dominantes
- Considerar factores de riesgo (edad, historial familiar)
- Síntomas cardíacos = prioridad máxima (ejemplo)
- Gravedad 5 = emergencia vital inmediata
- Validar estructura ANTES de responder
- Si los síntoma son muy variados y no tienen una relacion directa se mandara a Medicina General o Medicina Familiar según el caso

**Ejemplo válido:**
{"specialty": "Cardiología", "severity": 5}



Nota: 
1. No me des una respuesta diferente y no digas nada más en la respuesta 
2. Si consideras que lo que se describe es una area muy especifica que no se encuetra en las Especialidades válidas asignarás Medicina General por defecto
3. Si los síntomas presentados representan algo muy grave asignarás Medicina General
"""

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
                        "content": SYSTEM_PROMPT + f"\n\nEspecialidades válidas:\n{SPECIALTIES}"
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