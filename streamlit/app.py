
#Uretken Yapay Zeka ile Uygulama Geliştirme Eğitimi
#Modül 1: Streamlit ile Hızlı Prototipleme

#Streamlit101
#1 Streamlit kütüphanesini ekleme
import streamlit as st

#2 Streamlit uygulamasını başlatma
#st.write("Hello World") # ekrana yaz

#3 Streamlit ile sayfa bilgilerini düzenleme
# https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/ icon kodları burada
st.set_page_config(page_title="streamlit 101",page_icon=":coffee:") # set_page_config komutu streamlit için ilk komut olmak zorundadır


#4 Streamlit ile metin gösterme
st.write("yaygın metin gösterme komutu")

st.markdown("_biçimlendirilmiş metinler örn eğik yazı_") # eğik yazı yazalım

st.header("sayfa başlığı için header örneği")

st.subheader("altbaşlık: subheader örneği")

st.code("yazılanlar kod bloğu şeklinde görüntülenir for i in range(5):")

st.latex("matematiksel ifadeler icin latex seklinde yazılır: \log_k(n+m)")

#5 Streamlit ile multimedya gösterme
#st.image(image="miyuv.jpg")
#st.video(data=" ")
#st.audio(data="")

#6 Streamlit ile kullanıcı etkileşimi (button, radio, checkbox, slider, number input, file uploader)
'''st.write("lütfen bilgilerinizi girin:")
st.text_input(label="e postanızı girin")
st.text_input(label="şifrenizi girin:",type="password") #şifreyi maskeler

st.checkbox(label="şifremi unuttum")
st.divider()# divider yatay çizgi ile ekranı böler

st.number_input(label="yaşınızı girin",min_value=18,max_value=32,value=22)
st.slider(label="yaşınızı girin",min_value=18,max_value=32,value=22)

st.divider()

st.radio(label="statünüz nedir",options=["öğrenci","mezun"])# seçim yapmak için

st.button(label="giriş yap")

st.divider()

st.file_uploader(label="dosya yüklemek için tıklayınız")#kullanıcıdan dosya ister
'''
##############################################################################################################

#7 Streamlit ile ara yüz yerleşimi (col, tab, sidebar)
'''col1, col2 = st.columns(2)# iki sütun oluştur

with col1: # bu bloğun içindeki her şey 1. sütunu oluşturacak
    st.markdown("<h3><b> kullanıcı bilgileri </b> </h3>",unsafe_allow_html=True) # html gibi yazıyoruz
    st.text_input(label="e posta girin")
    st.text_input(label="şifre girin",type="password")
    st.checkbox(label="şifremi unuttum")
    st.divider()
    st.button(label="giriş yap")

with col2: # bu bloğun içindeki her şey 2. sütunu oluşturacak
    st.markdown("<h3><b> kullanım tercihleri </b> </h3>",unsafe_allow_html=True) # html gibi yazıyoruz
    st.divider()
    st.radio(label="hesap türü",options=["öğrenci","mezun"])
    st.slider(label="zaman aşım süresi(saniye)",min_value=3,max_value=30,value=5)
    st.file_uploader(label="özgeçmiş yükleyin")

'''


st.sidebar.markdown("<h4> Uygulamaya Hoşgeldiniz! </h4>",unsafe_allow_html=True)
st.sidebar.image("miyuv.jpg")
tab1, tab2 = st.tabs(["kullanıcı bilgileri","kullanım tercihleri"])# iki sütun yerine iki sekme gibi görünecek

with tab1: # bu bloğun içindeki her şey 1. sekmeyi oluşturacak
    eposta = st.text_input(label="e posta girin")
    sifre = st.text_input(label="şifre girin",type="password")
    st.checkbox(label="şifremi unuttum")
    st.divider()
    kaydet_buton = st.button(label="kaydet")

with tab2: # bu bloğun içindeki her şey 2. sekmeyi oluşturacak
    hesap_turu = st.radio(label="hesap türü",options=["öğrenci","mezun"])
    st.slider(label="zaman aşım süresi(saniye)",min_value=3,max_value=30,value=5)
    st.file_uploader(label="özgeçmiş yükleyin")

import json

if kaydet_buton:
    data = []
    data.append({"e posta":eposta})
    data.append({"sifre":sifre})

    if hesap_turu == "öğrenci":
        sure = 365
    elif hesap_turu == "mezun":
        sure = 30 

    data.append({"gecerlilik suresi": sure})

    with open("kullanici.txt","w") as file:
        file.write(json.dumps(data))

    st.balloons()
    st.success("dosyanız kaydedildi")
    st.write(f"belirlenen süre :{sure}")


#8 Streamlit bileşenleriyle program akışı

#9 Streamlit ile session state

