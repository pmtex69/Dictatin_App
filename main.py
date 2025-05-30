import os
from google.generativeai import GenerativeModel

# Obter a chave de API de uma variável de ambiente
API_KEY = os.getenv('GOOGLE_API_KEY') 
if not API_KEY:
    raise ValueError("GOOGLE_API_KEY environment variable not set.")

model = GenerativeModel(api_key=API_KEY)
# Resto do seu código que usa o modelo
