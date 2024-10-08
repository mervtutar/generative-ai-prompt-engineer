#conda install --file requirements.txt
#pip install -r requirements.txt
from openai import OpenAI
import os
from dotenv import load_dotenv

my_key = os.getenv("openai_apikey")
client = OpenAI(api_key=my_key)


AI_Response=client.chat.completions.create(
       model="gpt-4-1106-preview",
       temperature=0,
       max_tokens=256,
       messages=[
           {"role":"system","content":"Sen akıllı bir asistansın."},
           {"role":"user","content":"Mevsimler neden oluşur?"}
       ]
)

print(AI_Response.choices[0].message.content)



