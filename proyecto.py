#LIBRERIAS
import numpy as np
import streamlit as st
#FUNCIONES DE MODULOS
from lectura_csv import lectura
from Estatica1 import buscador_barrio,barrios5,grafico_barras
from Dinamica1 import menu,filtrar_barrios,buscar_ubicacion
from dinamica2_dias import slider,filtrar_dias,mostrar_tabla
from formato import formato_pagina


# ==================================================
# MAIN
# ==================================================
def main ():
         # ---------- LECTURA CSV ----------: 
         lista=lectura() 
         
         #----------Pregunta estática: 5 barrios con más alquileres----------
         barrios=buscador_barrio(lista)
         barrios_mayores= barrios5(barrios) 
         grafico=grafico_barras(barrios_mayores)

         
         #----------Pregunta dinámica: Mapeo de alquileres de X barrio----------
         opciones=menu(barrios) #st.menu
         alquileres_filtrados=filtrar_barrios(lista,opciones)
         if opciones != None:
               ubicacion= buscar_ubicacion(alquileres_filtrados)
               mapa=st.map(ubicacion,size=20, color="#0044ff")
               
         '''
         #----------Pregunta dinámica: Tabla de alquileres con X disponibilidad de días---------- 
         rango_dias= list(range(1,366))    
         dias=slider("Seleccionar cantidad de días",rango_dias) #st.select_slider
         lista_dias=filtrar_dias(lista,dias) 
         tabla=mostrar_tabla(lista_dias) #st.dataframe
         '''         

         #formato
         formato_pagina(grafico)


# ==================================================
# MAIN
# ==================================================         


main()






