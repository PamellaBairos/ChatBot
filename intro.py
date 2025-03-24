import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()


api_key = os.getenv("APYKEY")

# Verificar se a API Key foi encontrada
if not api_key:
    raise ValueError("API_KEY não encontrada. Verifique o arquivo .env.")

# envia as requisições 
genai.configure(api_key=api_key)

descricao = """
Você é um assistente especializado em salão de beleza e saúde dos cabelos.
Responda apenas perguntas relacionadas a esse tema.
Se uma pergunta estiver fora desse escopo, informe educadamente que não pode responder.
Você deve manter um tom respeitoso e obdecer as diretrizes éticas.
Sempre faça recomendaçoes em relação aos produtos como se você fosse um profissional qualificado. 
Após o final da resposta, você deve informar que sempre é necessario procurar um profissional qualificado para retirar as duvidas.
"""


gemini = genai.GenerativeModel(
    model_name="gemini-1.5-flash-002",
    system_instruction=descricao,
)

chat = gemini.start_chat()

print("\n💇‍♀️ Assistente de Salão de Beleza ativado! Pergunte sobre cuidados capilares.\n")

historico_respostas = []
contador = 0

while True:
    user_input = input("Você: ")
    
    if user_input.lower() in ["sair", "exit", "bye"]:
        print("👋 Até mais! Cuide bem dos seus cabelos! 💆‍♀️")
        break
    
    response = chat.send_message(user_input)
    print("Bot:", response.text, "\n")
    
    historico_respostas.append(response.text)
    contador += 1
    
    if contador % 3 == 0:
        resumo = chat.send_message("Resuma as últimas três respostas de forma clara e objetiva.")
        print("\n📌 Resumo das últimas interações:\n", resumo.text, "\n")
