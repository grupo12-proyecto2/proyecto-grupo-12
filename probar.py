import csv

def lectura():
        i=0
        lista_alquileres = []

        #GUARDAR DATOS EN LISTAS
        with open ("listings-San Francisco.csv", newline='') as csvfile:
                 archivo =csv.DictReader(csvfile, delimiter=',', quotechar='"') 
                 for linea in archivo:
                         lista_alquileres.append(linea)
        return lista_alquileres


              
