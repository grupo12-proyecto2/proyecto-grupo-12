import streamlit as st

def slider (frase,rango):
     cantidad = st.select_slider(
       frase,
       options=rango)
     return cantidad

def filtrar_dias(lista,dias):
     lista_filtrada=[]
     for linea in lista:
         if int(linea ["availability_365"])>=dias:
                lista_filtrada.append(linea)
     return lista_filtrada 
     

def mostrar_tabla(lista_filtrada):
     tabla=st.dataframe(lista_filtrada)
     return tabla
          

    

