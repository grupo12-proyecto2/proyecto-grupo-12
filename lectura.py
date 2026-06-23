import codecs

def crear_diccionario (linea1,flag=0):
 '''
 Representamos datos CSV, previamente almacenados en una lista, en un diccionario.
 Cada dato corresponde a cada categoría del archivo CSV.
 Clave: Categoría 
 Valor: Dato correspondiente
 PREGUNTA: Poner cada categoría, aunque algunas no se usen?
 linea1: Lista
 crear_diccionario: Lista -> Diccionario
 El parametro linea1 representa una lista, cuyos elementos serán almacenados
 en un diccionario.

 Ejemplos:
 crear_diccionario   
 PREGUNTA: Es necesario poner ejemplos de esto? Es posible probar esta funcion?
 '''
 x=0
 #Diccionario base
 diccionario_alquileres = {} 
 
 while  x <= len(linea1):
        if flag == 0:
                diccionario_alquileres[linea1[x]]=" "
                x=x+1
        else:
                claves=list(diccionario_alquileres.keys())
                diccionario_alquileres[claves[x]]=linea1[x] #Es necesario guardar la primer linea?
                x=x+1
 return diccionario_alquileres

 
#Lectura del archivo
def Lectura_Archivo (): 
 '''
 Representamos un archivo CSV, con una lista de diccionarios.
 Cada diccionario representa la información de un alquiler,
 es decir, de una línea del archivo CSV.
 Cada columna del archivo está representada en una clave del diccionario.

 lectura_Archivo: None -> Lista
        
 '''
 lista_alquileres = []
 i=0
 archivo1 = open ("Listing-prueba.csv")
 for linea in archivo1:
         linea=linea.strip("\n")
         linea=linea.split(",")
         if i>=1:
                 lista_alquileres.append(crear_diccionario(linea,1))
         if i==0:
                 crear_diccionario(linea,0)                 
                 i=i+1
 archivo1.close() #CIERRE 
 return lista_alquileres

