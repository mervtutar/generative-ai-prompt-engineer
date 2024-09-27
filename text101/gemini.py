import google.generativeai as genai
import os
from dotenv import load_dotenv


load_dotenv()

my_key=os.getenv("google_apikey")

genai.configure(api_key=my_key)

client = genai.GenerativeModel(
    model_name="gemini-1.5-flash"
)

def generate_response(prompt):

    chat = client.start_chat(history=[])
    AI_Response = chat.send_message(
        "Uçaklar nasıl üretilir?",
        generation_config= genai.GenerationConfig(
            temperature=0,
            max_output_tokens=256
        )
    )
    return AI_Response.text

# print(AI_Response.text)
# print("*"*100)
# print(chat.history)

import streamlit as st

st.header("Gemini ile sohbet edin")
st.divider()


prompt = st.text_input("Mesajınızı giriniz:")
submit_buton = st.button("gönder")

if submit_buton:

    response=generate_response(prompt)
    st.markdown(response)



# AI_Response = client.generate_content(
#     "Uçaklar nasıl üretilir?", #completion/generation
#     generation_config= genai.GenerationConfig(
#         temperature=0, # controls the randomness of the output
#         max_output_tokens=256 #  sets the maximum number of tokens to include in a candidate
#     )
# )

# print(AI_Response.text)
