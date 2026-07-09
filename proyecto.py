#LIBRERIAS
import numpy as np
import streamlit as st
#FUNCIONES DE MODULOS
from lectura_csv import lectura
from Estatica1 import buscador_barrio,barrios5,grafico_barras
from Dinamica1 import filtrar_barrios,buscar_ubicacion
from dinamica2_dias import filtrar_dias
from Dinamica3 import filtrar_por_habitacion
from Dinamica3 import tipo_habitaciones

# ==================================================
# MAIN
# ==================================================
def main ():
         # ---------- LECTURA CSV ----------: 
         lista=lectura("listings-San Francisco.csv")
          

         #---------- Formato de página ----------
         col1, col2 = st.columns(2,gap="large")

         #----------PREGUNTA ESTÁTICA: 5 barrios con más alquileres----------
         barrios=buscador_barrio(lista,"neighbourhood")
         barrios_mayores= barrios5(barrios,5) 
         grafico_alquileres = grafico_barras(barrios_mayores,"Cantidad de alquileres",'Los 5 barrios con más alquileres')

         #----------PREGUNTA ESTÁTICA: 5 barrios con más alquileres----------
         reseñas = buscador_barrio(lista,"number_of_reviews")
         reseñas_mayores = barrios5(reseñas,10)
         grafico_reseñas = grafico_barras(reseñas_mayores,"Cantidad de reseñas","Los 10 alquileres con más reseñas")
         
         #----------PREGUNTA DINÁMICA: Mapeo de alquileres----------
         col1.subheader("Mapa de alquileres por barrio")
         opcion=col1.selectbox("Seleccione un barrio",barrios) #Despliegue de menú y guarda
         alquileres_filtrados=filtrar_barrios(lista,opcion)
         ubicacion= buscar_ubicacion(alquileres_filtrados)
         col1.map(ubicacion,size=20, color="#0044ff")

         #----------PREGUNTA DINÁMICA: Tabla de alquileres con X disponibilidad de días---------- 
         rango_dias= list(range(1,366))
         col2.subheader("Disponibilidad de alquileres según días disponibles")    
         dias = col2.select_slider("Cantidad de días",rango_dias) 
         lista_dias=filtrar_dias(lista,dias)
         col2.write(f"Alquileres disponibles con {dias} días disponibles")
         col2.dataframe(lista_dias)
         #---------PREGUNTA DINAMICA: Tabla de alquileres con x tipo de habitacion--------
         obtener_habitaciones = tipo_habitaciones(lista)
         habitaciones = col2.multiselect("Seleccione uno o más tipos de habitación",obtener_habitaciones)
         lista_habitaciones = filtrar_por_habitacion(lista, habitaciones)
         col2.dataframe(lista_habitaciones)

         
         #----------Muestra de Gráfico----------
         col1.subheader("ESTADISTICA: Los 5 barrios con mas alquileres")
         col1.pyplot (grafico_alquileres)
         col1.pyplot (grafico_reseñas)
# ==================================================
# MAIN
# ==================================================         

#LLAMADO DE MAIN
main()






