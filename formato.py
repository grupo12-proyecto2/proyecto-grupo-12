import streamlit as st

def formato_pagina (mapa,grafico,menu,slider,tabla):
    col1, col2 = st.columns([1, 1])

    col1.subheader("Mapa")
    col1.map(mapa)
    col1.pyplot(grafico)

    col2.subheader("Seleccione un barrio")
    col2.menu_button(menu)
    col2.select_slider(slider)
    col2.dataframe(tabla)
    



