from google import genai
from google.genai import types
from dotenv import load_dotenv
import os
load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API"))
historico = []
instrucao = "Você é uma IA gentil"


while True:
    try:
        input_usuario = input("Digite para a IA: ")
        mensagem_usuario ={"role": "user", "parts": [{"text": input_usuario}]}
        historico.append(mensagem_usuario)
        response = client.models.generate_content(
            model="gemini-3.5-flash",
            contents=historico,
            config=types.GenerateContentConfig(
                system_instruction=instrucao
            )
        )
        mensagem_ia = {"role": "model", "parts": [{"text": response.text}]}
        historico.append(mensagem_ia)
        if len(historico) > 10:
            historico = historico[-10:]
        print(response.text)
    except Exception as error:
        print(f"Erro: {error}")