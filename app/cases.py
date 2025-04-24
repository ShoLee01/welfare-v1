from typing import List
from pydantic import BaseModel

class PatientData(BaseModel):
    symptoms: str
    age: int
    medical_history: List[str]
    family_history: List[str]
    gender: str

# Caso 1 (Cardiología)
PatientData(
    symptoms="palpitaciones, mareo al levantarse",
    age=48,
    medical_history=["hipertensión"],
    family_history=[],
    gender="femenino"
)

# Caso 2 (Neumología)
PatientData(
    symptoms="tos con sangre, pérdida de peso",
    age=35,
    medical_history=["tabaquismo"],
    family_history=["cáncer de pulmón"],
    gender="masculino"
)

# Caso 3 (Pediatría)
PatientData(
    symptoms="fiebre alta, erupción cutánea",
    age=3,
    medical_history=[],
    family_history=[],
    gender="femenino"
)

# Caso 4 (Neurología)
PatientData(
    symptoms="pérdida de visión súbita en un ojo",
    age=28,
    medical_history=[],
    family_history=["esclerosis múltiple"],
    gender="masculino"
)

# Caso 5 (Ginecología)
PatientData(
    symptoms="sangrado vaginal irregular, dolor pélvico",
    age=42,
    medical_history=[],
    family_history=[],
    gender="femenino"
)

# Caso 6 (Medicina General)
PatientData(
    symptoms="fatiga, dolor muscular generalizado",
    age=67,
    medical_history=["artritis"],
    family_history=["diabetes"],
    gender="masculino"
)

# Caso 7 (Endocrinología)
PatientData(
    symptoms="sed excesiva, micción frecuente",
    age=15,
    medical_history=[],
    family_history=["diabetes tipo 1"],
    gender="femenino"
)

# Caso 8 (Gastroenterología)
PatientData(
    symptoms="heces negras alquitranadas, dolor abdominal",
    age=58,
    medical_history=["úlcera péptica"],
    family_history=[],
    gender="masculino"
)

# Caso 9 (Traumatología)
PatientData(
    symptoms="dolor lumbar intenso tras caída",
    age=72,
    medical_history=["osteoporosis"],
    family_history=[],
    gender="femenino"
)

# Caso 10 (Psiquiatría)
PatientData(
    symptoms="ideas suicidas, insomnio persistente",
    age=24,
    medical_history=[],
    family_history=["depresión"],
    gender="no binario"
)

# Caso 11 (Dermatología)
PatientData(
    symptoms="lesiones ampollosas pruriginosas",
    age=19,
    medical_history=["dermatitis atópica"],
    family_history=[],
    gender="masculino"
)

# Caso 12 (Urología)
PatientData(
    symptoms="dificultad para orinar, sangre en orina",
    age=65,
    medical_history=[],
    family_history=["cáncer de próstata"],
    gender="masculino"
)

# Caso 13 (Oftalmología)
PatientData(
    symptoms="visión borrosa repentina, moscas volantes",
    age=55,
    medical_history=["diabetes"],
    family_history=[],
    gender="femenino"
)

# Caso 14 (Otorrinolaringología)
PatientData(
    symptoms="pérdida auditiva unilateral, acúfenos",
    age=40,
    medical_history=[],
    family_history=[],
    gender="masculino"
)

# Caso 15 (Nutrición)
PatientData(
    symptoms="obesidad mórbida, dislipidemia",
    age=32,
    medical_history=[],
    family_history=[],
    gender="femenino"
)

# Caso 16 (Geriatría)
PatientData(
    symptoms="desorientación temporal, caídas recurrentes",
    age=85,
    medical_history=["demencia"],
    family_history=[],
    gender="masculino"
)

# Caso 17 (Medicina Familiar)
PatientData(
    symptoms="tos persistente, fiebre baja",
    age=30,
    medical_history=[],
    family_history=[],
    gender="femenino"
)

# Caso 18 (Cardiología)
PatientData(
    symptoms="edema en miembros inferiores, disnea nocturna",
    age=70,
    medical_history=[],
    family_history=["insuficiencia cardíaca"],
    gender="masculino"
)

# Caso 19 (Neurología)
PatientData(
    symptoms="temblor en reposo, rigidez muscular",
    age=68,
    medical_history=[],
    family_history=["Parkinson"],
    gender="femenino"
)

# Caso 20 (Psicología)
PatientData(
    symptoms="ansiedad social, ataques de pánico",
    age=22,
    medical_history=[],
    family_history=[],
    gender="femenino"
)

# Caso 21 (Obstetricia)
PatientData(
    symptoms="contracciones regulares cada 5 minutos",
    age=29,
    medical_history=["embarazo de 38 semanas"],
    family_history=[],
    gender="femenino"
)

# Caso 22 (Neumología)
PatientData(
    symptoms="sibilancias, opresión torácica",
    age=14,
    medical_history=["asma"],
    family_history=[],
    gender="masculino"
)

# Caso 23 (Endocrinología)
PatientData(
    symptoms="intolerancia al frío, piel seca",
    age=45,
    medical_history=[],
    family_history=["hipotiroidismo"],
    gender="femenino"
)

# Caso 24 (Traumatología)
PatientData(
    symptoms="dolor de rodilla al subir escaleras",
    age=50,
    medical_history=["obesidad"],
    family_history=[],
    gender="masculino"
)

# Caso 25 (Gastroenterología)
PatientData(
    symptoms="ictericia, heces claras",
    age=37,
    medical_history=[],
    family_history=[],
    gender="femenino"
)

# Caso 26 (Urología)
PatientData(
    symptoms="cólico renal unilateral",
    age=33,
    medical_history=["litiasis renal"],
    family_history=[],
    gender="masculino"
)

# Caso 27 (Dermatología)
PatientData(
    symptoms="eritema migrans tras picadura de garrapata",
    age=27,
    medical_history=[],
    family_history=[],
    gender="femenino"
)

# Caso 28 (Oftalmología)
PatientData(
    symptoms="dolor ocular intenso con náuseas",
    age=60,
    medical_history=["glaucoma"],
    family_history=[],
    gender="masculino"
)

# Caso 29 (Medicina General)
PatientData(
    symptoms="mareo postural, debilidad generalizada",
    age=78,
    medical_history=["hipertensión"],
    family_history=[],
    gender="femenino"
)

# Caso 30 (Psiquiatría)
PatientData(
    symptoms="alucinaciones auditivas, paranoia",
    age=19,
    medical_history=[],
    family_history=["esquizofrenia"],
    gender="masculino"
)