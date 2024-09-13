# conda install --file requirements.txt or pip install -r requirements.txt
import streamlit as st
import pandas as pd

st.header("session state pratik kullanım")

if "satir" not in st.session_state:
    st.session_state.satir=10

dataframe = pd.read_csv("accounts.csv", sep = ",") # veriler virgülle ayrılmış
st.table(dataframe.head(st.session_state.satir))# ekranda 10 satırlık girdi göstericek


def artir(): # callback fonklar oluştur
    st.session_state.satir += 1

def dusur():
    st.session_state.satir -= 1

arttir_btn = st.button(label="arttır 👆", on_click=artir)
dusur_btn = st.button(label="düşür 👇",on_click=dusur)

st.divider()
st.header(st.session_state.satir)


# streamlitte sayfadaki herhangi bir değişiklik, bir butona basmak vs tüm kodun en başta çalışmasını sağlar


# import streamlit as st


# st.session_state.mesaj = "bilgilendirme mesaji" #session_state bir container gibi düşünebiliriz streamlit için
# st.session_state.yil = 2024 
# st.session_state["kullanici adi"] = "miuul"

# gunler = ["pzt","sali","çarş","perş","cuma"]
# st.session_state.liste = gunler

# st.write(st.session_state)

# st.session_state.yil += 10 #2034

# st.write(st.session_state)

# st.session_state.eposta = st.text_input(label="e posta girin:")
# st.text_input(label="sifre girin", type="password",key="sifre") 

# btn = st.button(label="görüntüle")

# if btn:
#     st.info(st.session_state.eposta)
#     st.info(st.session_state.sifre)



