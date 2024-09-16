import cohere
import os
from dotenv import load_dotenv

load_dotenv()

my_key = os.environ.get("cohere_apikey")

client = cohere.Client( api_key=my_key)

AI_Response = client.chat(
    model = "command",
    temperature=0,
    max_tokens=256,
    chat_history=[
        {"role": "USER","message":"Adı Hürjet olan uçak nereye aittir?"},
        {"role":"CHATBOT","message":"Hürjet Türkiye'ye ait bir jet eğitim ve yakın hava desteği uçagıdır."}

    ],
    message="Hangi amaçla geliştirilmiştir?"
)

print(AI_Response.text)