import streamlit as st

def slider ():
     dias = st.select_slider(
       "Selecciona la cantidad de dias",
       options=list (range (1,366))
       ,
     )
     st.write("La cantidad de dias es:  ",dias) 
     return dias

def filtrar_dias(lista,dias):
     lista_filtrada=[]
     for linea in lista:
         if int(linea ["availability_365"])>=dias:
                lista_filtrada.append(linea) 
     return lista_filtrada  
    

