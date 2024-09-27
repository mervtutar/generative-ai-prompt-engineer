import replicate
from dotenv import load_dotenv

load_dotenv()

prompt = "Uçaklar ne işe yarar?"
system_prompt = "Sen akıllı bir asistansın."

# Llama 2 70 B Chat

AI_Response = replicate.run(

    "meta/llama-2-70b-chat",
    input={
        "temperature":0.5,
        "max_new_tokens":256,
        "system_prompt":system_prompt,
        "prompt":prompt,
        "debug":False
    }

)
AI_Response = "".join(AI_Response)
print(AI_Response)
print("*"*100)

# Mixtral
#chat modeli değil (instruct), completion/generation modeli o yüzden system prompt a ihtiyaç yok
AI_Response = replicate.run(
    "mistralai/mixtral-8x7b-instruct-v0.1", # 8 adet 7 milyar parametreli model
    input = {
        "temperature":0.5,
        "max_new_tokens":256,
        "prompt":prompt,
        "debug":False
    }
)

AI_Response = "".join(AI_Response)
print(AI_Response)