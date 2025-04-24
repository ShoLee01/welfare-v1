# import os
# import time
# from typing import List
# from groq import Groq
# from pydantic import BaseModel, ValidationError



# def print_recommendation(recommendation: MedicalRecommendation):
#     print(f"\nRecomendación médica:")
#     print(f"Especialidad: {recommendation.specialty}")
#     print(f"Gravedad (1-5): {recommendation.severity}")

# # Ejemplo de uso
# patient_data = PatientData(
#     symptoms="sibilancias, opresión torácica",
#     age=14,
#     medical_history=["asma"],
#     family_history=[],
#     gender="masculino"
# )

# recommendation = get_medical_recommendation(patient_data)
# print_recommendation(recommendation)