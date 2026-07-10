#LIBRERIAS
import numpy as np
import streamlit as st
#FUNCIONES DE MODULOS
from lectura_csv import lectura
from Estatica1 import buscador_barrio,buscar_maximos,grafico_barras
from Estatica2 import buscador_reseñas
from Dinamica1 import filtrar_barrios,buscar_ubicacion
from dinamica2_dias import filtrar_dias
from Dinamica3 import filtrar_por_habitacion
from Dinamica3 import tipo_habitaciones
from Dinamica4 import filtro_ultimo_año

# ==================================================
# MAIN
# ==================================================
def main ():
         # ---------- LECTURA CSV ----------: 
         lista=lectura("listings-San Francisco.csv")
          

         #---------- Formato de página ----------
         st.set_page_config(layout="wide")
         col1, col2 = st.columns(2,gap="large")


         #----------PREGUNTA ESTÁTICA: 5 barrios con más alquileres----------
         barrios=buscador_barrio(lista,"neighbourhood")
         barrios_mayores= buscar_maximos(barrios,5) 
         grafico_alquileres = grafico_barras(barrios_mayores,"Cantidad de alquileres",'Los 5 barrios con más alquileres')

         #----------PREGUNTA ESTÁTICA: 5 barrios con más alquileres----------
         reseñas = buscador_reseñas(lista)
         reseñas_mayores = buscar_maximos(reseñas,10)
         grafico_reseñas = grafico_barras(reseñas_mayores,"Cantidad de reseñas","Los 10 alquileres con más reseñas")
         
         #----------PREGUNTA DINÁMICA: Mapeo de alquileres----------
         col1.subheader("Mapa de alquileres por barrio")
         opcion=col1.selectbox("Seleccione un barrio",barrios) #Despliegue de menú y guarda
         alquileres_filtrados=filtrar_barrios(lista,opcion)
        

         #----------PREGUNTA DINÁMICA: Reseñas en el último año----------
         fue_reseñada = col1.checkbox ("Con reseñas en el último año")
         alquileres_ultimo_año = filtro_ultimo_año (alquileres_filtrados,fue_reseñada)
         

         #----------PREGUNTA DINÁMICA: Tabla de alquileres con X disponibilidad de días---------- 
         rango_dias= list(range(1,366))
         col2.subheader("Filtro de alquileres")    
         dias = col2.select_slider("Cantidad de días",rango_dias) 
         lista_dias=filtrar_dias(lista,dias)
         
         
         #---------PREGUNTA DINAMICA: Tabla de alquileres con x tipo de habitacion--------
         obtener_habitaciones = tipo_habitaciones(lista)
         habitaciones = col2.multiselect("Seleccione uno o más tipos de habitación",obtener_habitaciones)
         lista_habitaciones = filtrar_por_habitacion(lista_dias, habitaciones)

         #----------Muestra de tabla-------------  
         col2.write("Alquileres disponibles con  los días y el tipo de habitación seleccionados") 
         col2.dataframe(lista_habitaciones)

         #----------Muestra de Mapa-------------
         ubicacion= buscar_ubicacion(alquileres_ultimo_año)
         col1.map(ubicacion,size=20, color="#0044ff")

         #----------Muestra de Gráfico----------
         col1.subheader("ESTADISTICAS")
         col1.pyplot (grafico_alquileres)
         col2.pyplot (grafico_reseñas)

# ==================================================
# MAIN
# ==================================================         

#LLAMADO DE MAIN
main()






