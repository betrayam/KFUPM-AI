import streamlit as st
import json
import requests  # pip install requests
from streamlit_lottie import st_lottie  # pip install streamlit-lottie

# GitHub: https://github.com/andfanilo/streamlit-lottie
# Lottie Files: https://lottiefiles.com/




def home():
    def load_lottiefile(filepath: str):
        with open(filepath, "r") as f:
            return json.load(f)


    def load_lottieurl(url: str):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    c1, c2, c3 = st.columns([1,1,1], vertical_alignment="center")
    lottie_hello = load_lottieurl("https://lottie.host/057e0efe-27c7-4397-840c-f1f25b8a682a/6Dw9TLkyW5.json")
    with c2:
        st_lottie(
            lottie_hello,
            speed=1,
            reverse=False,
            loop=True,
            quality="low", # medium ; high
            #renderer="svg", # canvas
            height=300,
            width=300,
            key=None,

        )
    a1, a2, a3 = st.columns([1,5,1], vertical_alignment="center")
    with a2:
        #st.title("Your AI for your Documents")
        st.markdown("<h1 style='text-align: center;'>Your AI for your course documents</h1>", unsafe_allow_html=True)
    with a2:
        st.markdown("<h4 style='text-align: center;'>From text to clarity in seconds, AI summaries and answers at your command. Transform your documents effortlessly.</h4>", unsafe_allow_html=True)
    with a2:
        st.markdown("<h6 style='text-align: center;'>Here to help you in: </h6>", unsafe_allow_html=True)
    col0 ,col1, col2, col3 = st.columns([1,1,1,1], vertical_alignment="center")
    lottie_book = load_lottieurl("https://lottie.host/08ee5464-faa7-4404-b455-419a1e37817a/ynP85Jx5P5.json")
    lottie_fin = load_lottieurl("https://lottie.host/9901e242-2988-4b49-8af1-df12c5fd3c09/MP9HCz7jSA.json")
    lottie_sch = load_lottieurl("https://lottie.host/1897e516-aea8-4525-ac96-c54becc256dc/885y6Jrhy0.json")
    lottie_gen = load_lottieurl("https://lottie.host/f716f72e-08d6-4026-94c6-94543a98c381/T4mz6F7KHx.json")
    with col0:
        st_lottie(
            lottie_book,
            speed=1,
            reverse=False,
            loop=True,
            quality="low", # medium ; high
            #renderer="svg", # canvas
            height=250,
            width=250,
            key=None,

        )    
    with col1:
        st_lottie(
            lottie_fin,
            speed=1,
            reverse=False,
            loop=True,
            quality="low", # medium ; high
            #renderer="svg", # canvas
            height=250,
            width=250,
            key=None,

        )    
            
    with col2:
        st_lottie(
            lottie_sch,
            speed=1,
            reverse=False,
            loop=True,
            quality="low", # medium ; high
            #renderer="svg", # canvas
            height=250,
            width=250,
            key=None,

        )   
    with col3:
        st_lottie(
            lottie_gen,
            speed=1,
            reverse=False,
            loop=True,
            quality="low", # medium ; high
            #renderer="svg", # canvas
            height=250,
            width=250,
            key=None,

        )  
    #lottie_coding = load_lottiefile("lottiefile.json")  # replace link to local lottie file
    