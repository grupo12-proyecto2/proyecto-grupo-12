from lectura import crear_diccionario
from lectura_csv import lectura
from Estatica1 import buscador_barrio,barrios5
from Dinamica1 import filtrar_barrios,buscar_ubicacion
from dinamica2_dias import filtrar_dias
from Dinamica3 import filtrar_por_habitacion
from Dinamica3 import tipo_habitaciones


#testing
'''
def test_crear_diccionario():
    """
    funcion de prueba de la funcion crear_diccionario
    """
    linea = ["958","Bright Modern Garden Unit - 1BR/1BTH","1169","1462506189282101689",
             "Holly","","Western Addition","37.77028","-122.43317","Entire home/apt","",
             "2,507","2025-11-15","2.54","1","228","41","STR-0006854"]

    dic = crear_diccionario(linea)

    assert dic["id"] == "958"
    assert dic["name"] == "Bright Modern Garden Unit - 1BR/1BTH"
    assert dic["neighbourhood"] == "Western Addition"
    assert dic["license"] == "STR-0006854"
'''
#========================================================
#           testing de buscador_barrio()
#========================================================
def test_buscador_barrio():
    #funcion de prueba de la funcion busacador_barrio
    assert buscador_barrio([])=={} 
    assert buscador_barrio([{"neighbourhood":"Bernal Heights"}])=={"Bernal Heights":1 }
    assert buscador_barrio([{"neighbourhood":"Crocker Amazon","price": 100,"room_type":"Entire home/apt"},
            {"neighbourhood":"Downtown/Civic Center","price":85,"room_type":"Private room"},
            {"neighbourhood":"Crocker Amazon","price":120,"room_type":"Entire home/apt"}])=={"Crocker Amazon":2,"Downtown/Civic Center":1} 
    alquileres = [
        {"neighbourhood": "Western Addition"},
        {"neighbourhood": "Bernal Heights"},
        {"neighbourhood": "Haight Ashbury"},
        {"neighbourhood": "Western Addition"},
        {"neighbourhood": "Bayview"},
        {"neighbourhood": "Nob Hill"},
        {"neighbourhood": "Bayview"},
        {"neighbourhood": "Bayview"},
        {"neighbourhood": "Bayview"},
     ]
    assert buscador_barrio(alquileres) == {
        "Western Addition":2,
        "Bernal Heights":1,
        "Nob Hill": 1,
        "Haight Ashbury": 1,
        "Bayview":4}

def test_barrios5():
    assert barrios5({})=={}
    assert barrios5({"Mission":100,"Wester Addition":50,"Pacific Heights":40,
                     "Dowtown/Civic Center":30,"Bernal Heights":20,"Haight Ashbury":10,
                     "Noe Valley":5})=={"Mission":100,"Wester Addition":50,"Pacific Heights":40,
                                         "Dowtown/Civic Center":30,"Bernal Heights":20}
    assert barrios5({"Mission":100,"Dowtown/Civic Center":30})=={"Mission":100,"Dowtown/Civic Center":30}


#===============================================================
#                Testing de filtrar_barrios
#===============================================================
def test_filtrar_barrios():
    """
    funcion de prueba de la funcion filtrar_barrios
    """
    assert filtrar_barrios([{"neighbourhood": "Nob hill"},{"neighbourhood": "Nob hill"}] , "Potrero hill") == []
    assert filtrar_barrios ([{"neighbourhood": "Nob hill"},{"neighbourhood": "Potrero hill"}] , "Nob hill") == [{"neighbourhood": "Nob hill"}]
    assert filtrar_barrios ([] , "Potrero hill") == []
#===============================================================
#               Testing de buscar_ubicacion   
#===============================================================
def test_buscar_ubicacion():
    """
    funcion de prueba de la funcion buscar_ubicacion
    """
    lista = [{"latitude": "37.77", "longitude": "-122.42"},{"latitude": "37.78", "longitude": "-122.43"}]
    assert buscar_ubicacion(lista) == {"lat": [37.77, 37.78],"lon": [-122.42, -122.43]}

    lista2=[]
    assert buscar_ubicacion(lista2) == {'lat': [], 'lon': []}
    
    lista3=[{"neighbourhood": "Nob hill"},{"neighbourhood": "Nob hill"}]
    assert buscar_ubicacion(lista3) == {'lat': [], 'lon': []}

#===============================================================
#               Testing de filtrar_dias   
#===============================================================
def test_filtrar_dias():
    lista= [{"availability_365": "276", "reviews_last_year": "2", "status": ""},
    {"availability_365": "310", "reviews_last_year": "0", "status": "pending"},
    {"availability_365": "211", "reviews_last_year": "1", "status": ""}]

    assert filtrar_dias (lista,300) == [{"availability_365": "310", "reviews_last_year": "0", "status": "pending"}]
    assert filtrar_dias (lista,200) == [{"availability_365": "276", "reviews_last_year": "2", "status": ""},
       {"availability_365": "310", "reviews_last_year": "0", "status": "pending"},
       {"availability_365": "211", "reviews_last_year": "1", "status": ""}]
    assert filtrar_dias ([],20) == []

def test_lectura ():
    assert lectura("Listing-prueba.csv") == [{
        "id": "958",
        "name": "Bright Modern Garden Unit - 1BR/1BTH",
        "host_id": "1169",
        "host_profile_id": "1462506189282101689",
        "host_name": "Holly",
        "neighbourhood_group": "",
        "neighbourhood": "Western Addition",
        "latitude": "37.77028",
        "longitude": "-122.43317",
        "room_type": "Entire home/apt",
        "price": "",
        "minimum_nights": "2",
        "number_of_reviews": "507",
        "last_review": "2025-11-15",
        "reviews_per_month": "2.54",
        "calculated_host_listings_count": "1",
        "availability_365": "228",
        "number_of_reviews_ltm": "41",
        "license": "STR-0006854"
        },
        {
        "id": "5858",
        "name": "Creative Sanctuary",
        "host_id": "8904",
        "host_profile_id": "1462506623299518225",
        "host_name": "Philip Jonathon",
        "neighbourhood_group": "",
        "neighbourhood": "Bernal Heights",
        "latitude": "37.74474",
        "longitude": "-122.42089",
        "room_type": "Entire home/apt",
        "price": "",
        "minimum_nights": "30",
        "number_of_reviews": "105",
        "last_review": "2017-08-06",
        "reviews_per_month": "0.52",
        "calculated_host_listings_count": "1",
        "availability_365": "365",
        "number_of_reviews_ltm": "0",
        "license": ""
        },
        {
        "id": "8142",
        "name": "*FriendlyRoom Apt. Style -UCSF/USF - San Francisco",
        "host_id": "21994",
        "host_profile_id": "1462506956810615042",
        "host_name": "Aaron",
        "neighbourhood_group": "",
        "neighbourhood": "Haight Ashbury",
        "latitude": "37.76555",
        "longitude": "-122.45213",
        "room_type": "Private room",
        "price": "",
        "minimum_nights": "32",
        "number_of_reviews": "10",
        "last_review": "2023-07-30",
        "reviews_per_month": "0.07",
        "calculated_host_listings_count": "20",
        "availability_365": "362",
        "number_of_reviews_ltm": "0",
        "license": ""
        }]
        
#===============================================================
#               Testing de filtrar_por_habitacion   
#===============================================================
def test_filtrar_por_habitacion():
    lista=[{"room_type": "Private room","neighbourhood": "Nob hill"},
    {"room_type": "Shared room","neighbourhood": "Nob hill"},
    {"room_type": "Entire home/apt", "neighbourhood": "Nob hill"}]
    assert filtrar_por_habitacion(lista,["Private room","Shared room","Entire home/apt"]) == lista
    assert filtrar_por_habitacion(lista,["Private room","Shared room"])==[{"room_type": "Private room","neighbourhood": "Nob hill"},
    {"room_type": "Shared room","neighbourhood": "Nob hill"}]
    assert filtrar_por_habitacion(lista,["Private room"]) == [{"room_type": "Private room","neighbourhood": "Nob hill"}]
    assert filtrar_por_habitacion([],["Private room"])== []
    assert filtrar_por_habitacion (lista,[])== []

#===============================================================
#               Testing de tipo_habitaciones  
#===============================================================
def test_tipo_habitaciones():
    lista=[{"room_type": "Private room", "neighbourhood": "Nob hill"},
    {"room_type": "Shared room", "neighbourhood": "Nob hill"},
    {"room_type": "Shared room", "neighbourhood": "Nob"}] 
    assert tipo_habitaciones(lista) == ["Private room","Shared room"]
    assert tipo_habitaciones([]) == []
    assert tipo_habitaciones ([{ "neighbourhood": "Nob hill"}]) == []
        

         
