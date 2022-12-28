import time

import pandas as pd
import streamlit as st
import plotly.express as px

st.write("HELLO THERE")

tab1, tab2 = st.tabs(['Ankieta', 'Staty'])


def onButtonClick():
    if name == "" or surname == "":
        st.info("Uzupelnij pola")
    else:
        st.success("Udalo sie dodac ankiete")


with tab1:
    st.text("Uzupelnij niniejsza ankiete")
    name = st.text_input('Wpisz imie')
    surname = st.text_input('Wpisz nazwisko')

    st.button("BRUH", on_click=onButtonClick)

with tab2:
    st.text("DANE")
    uploaded_file = st.file_uploader("Wrzuc plik CSV", type=".csv")

    if uploaded_file is not None:
        with st.spinner("Wait for it..."):
            df = pd.read_csv(uploaded_file)
            time.sleep(1)

            selected = st.radio(
                "Wybierz wizualizacje",
                ('BOX - Gender od Birthdate', 'HEATMAP - Gender od Campaign')
            )

            if selected == 'BOX - Gender od Birthdate':
                st.plotly_chart(px.box(df, x='gender', y='birthdate'))
            else:
                st.plotly_chart(px.density_heatmap(df, x='gender', y='campaign'))
