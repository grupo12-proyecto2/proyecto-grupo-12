
import numpy as np
import streamlit as st

def main ():
         #Lectura del archivo: 
         from lectura import Lectura_Archivo
         #lista=Lectura_Archivo()
         from probar import lectura
         lista=lectura() #VERSION ALTERNATIVA (PREGUNTAR AL PROFE)
         
         #Pregunta Estática: Mostrar los 5 barrios con más alquileres
         from Estatica1 import buscador_barrio,barrios5,grafico_barras
         barrios=buscador_barrio(lista)
         barrios_mayores= barrios5(barrios) 
         st.pyplot(grafico_barras(barrios_mayores))
         #Pregunta dinamica: mostrar en el mapa los alquileres
         from Dinamica1 import menu,filtrar_barrios,buscar_ubicacion
         opciones=menu(barrios)
         st.write(filtrar_barrios(lista,opciones))
         alquileres_filtrados=filtrar_barrios(lista,opciones)
         if opciones != None:
               ubicacion= buscar_ubicacion(alquileres_filtrados)
               #Pregunta Dinámica: Mostrar en el mapa los alquileres de X barrio
               st.map(ubicacion,size=20, color="#0044ff")
               st.write(ubicacion)
               
         
main()




