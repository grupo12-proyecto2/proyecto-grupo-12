import codecs

def crear_diccionario (linea:list[int|str|float],campos:list[str]):
 '''
 Representamos una linea del CSV (lista), con un diccionario.
 El diccionario queda definido por la estructura {Campo:Valor}
 Campo: String ("id","neighbourhood",etc)
 Valor: Int|String|Float ("958","Western Addition",etc)

 linea: Lista [int|str|float]
 campos: Lista [str]

 crear_diccionario: Lista -> Diccionario
 El parametro linea1 representa una lista, cuyos elementos serán almacenados
 en un diccionario.

 Ejemplos:
 crear_diccionario(["958", "Bright Modern Garden Unit - 1BR/1BTH", "1169", "1462506189282101689", "Holly", "", "Western Addition", "37.77028",
                   "-122.43317", "Entire home/apt", "", "2", "507", "2025-11-15", "2.54", "1", "228", "41", "STR-0006854"],["id", "name", "host_id", "host_profile_id", 
                   "host_name", "neighbourhood_group", "neighbourhood", "latitude", "longitude", "room_type", "price", "minimum_nights", "number_of_reviews", "last_review",
                   "reviews_per_month", "calculated_host_listings_count", "availability_365", "number_of_reviews_ltm", "license"])   
                   == {"id": "958", "name": "Bright Modern Garden Unit - 1BR/1BTH", "host_id": "1169", "host_profile_id": "1462506189282101689", "host_name": "Holly", 
                   "neighbourhood_group": "", "neighbourhood": "Western Addition", "latitude": "37.77028", "longitude": "-122.43317", "room_type": "Entire home/apt", "price": ""
                   , "minimum_nights": "2", "number_of_reviews": "507", "last_review": "2025-11-15", "reviews_per_month": "2.54", "calculated_host_listings_count": "1", "availability_365": "228",
                    "number_of_reviews_ltm": "41", "license": "STR-0006854"}
 crear_diccionario(["10537", "Elegant & Cozy w/City views. Private room: Purple", "36752", "1462507288958203289", "Teresa", "", "Bayview", "37.7175",
                   "-122.39698", "Private room", "", "1", "46", "2025-11-07", "0.24", "3", "365", "12", "2022-011003STR"], ["id", "name", "host_id", "host_profile_id",
                   "host_name", "neighbourhood_group", "neighbourhood", "latitude", "longitude", "room_type", "price", "minimum_nights", "number_of_reviews", "last_review",
                   "reviews_per_month", "calculated_host_listings_count", "availability_365", "number_of_reviews_ltm", "license"])
                   == {"id": "10537", "name": "Elegant & Cozy w/City views. Private room: Purple", "host_id": "36752", "host_profile_id": "1462507288958203289", "host_name": "Teresa",
                   "neighbourhood_group": "", "neighbourhood": "Bayview", "latitude": "37.7175", "longitude": "-122.39698", "room_type": "Private room", "price": "",
                   "minimum_nights": "1", "number_of_reviews": "46", "last_review": "2025-11-07", "reviews_per_month": "0.24", "calculated_host_listings_count": "3",
                   "availability_365": "365", "number_of_reviews_ltm": "12", "license": "2022-011003STR"}                  
 '''
 diccionario = {}
 x = 0

 for elemento in linea:
         if x < len(campos):
                 diccionario[campos[x]] = elemento
                 x=x+1
 return diccionario                
 
#Lectura del archivo
def Lectura_Archivo (): 
 '''
 Representamos un archivo CSV, con una lista de diccionarios.

 Cada diccionario representa la información de un alquiler,
 es decir, de una línea del archivo CSV.

 lista_alquileres: List[Dict]

 Diccionario: Dict{Campo:Valor}
 Campo: String ("id","neighbourhood",etc)
 Valor: Int|String|Float ("958","Western Addition",etc)

 lectura_Archivo: None -> Lista
        
 '''
 lista_alquileres = []
 i=0
 archivo1 = open ("Listing-prueba.csv")

 for linea in archivo1:
         linea=linea.strip("\n")
         linea=linea.split(",")
         if i == 0:
                 campos=linea
                 i=i+1
         else:
                 lista_alquileres.append(crear_diccionario(linea,campos))
 archivo1.close() #CIERRE 
 return lista_alquileres

