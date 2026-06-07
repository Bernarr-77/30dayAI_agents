from google import genai
from google.genai import types
from dotenv import load_dotenv
import os
load_dotenv()
try:
    client = genai.Client(api_key=os.getenv("GEMINI_API"))
    instrucao = "Você é uma IA gentil"
    input_usuario = "OI como vc esta"
    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=input_usuario,
        config=types.GenerateContentConfig(
            system_instruction=instrucao
        )
    )
    print(response)
except Exception as error:
    print(f"Erro: {error}")