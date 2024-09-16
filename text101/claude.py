import anthropic
import os
from dotenv import load_dotenv

load_dotenv()

my_key=os.environ.get("anthropic_apikey")
#print(my_key)
client = anthropic.Anthropic(api_key=my_key)

def generate_response(prompt):

    AI_Response = client.messages.create(
        model = "claude-3-haiku-20240307",
        temperature = 0.9,
        max_tokens = 256,
        messages = [
            {"role":"user", "content":prompt}
        ]
    )

    return AI_Response.content[0].text


import streamlit as st

st.header("Claude ile sohbet edin")
st.divider()


prompt = st.text_input("Mesajınızı giriniz:")
submit_buton = st.button("gönder")

if submit_buton:

    response=generate_response(prompt)
    st.markdown(response)
    
