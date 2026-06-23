from lectura import crear_diccionario
from Estatica1 import buscador_barrio
from Dinamica1 import filtrar_barrios
from Dinamica1 import buscar_ubicacion
#testing

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

def test_buscador_barrio():
    """
    funcion de prueba de la funcion busacador_barrio
    """
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


def test_filtrar_barrios():
    """
    funcion de prueba de la funcion filtrar_barrio
    """
    lista = [{"neighbourhood": "Nob Hill"},{"neighbourhood": "Bayview"},{"neighbourhood": "Nob Hill"}]

    assert filtrar_barrios(lista, "Nob Hill") == [{"neighbourhood": "Nob Hill"},{"neighbourhood": "Nob Hill"}]
#Testing buscar_ubicacion   
def test_buscar_ubicacion():
    """
    funcion de prueba de la funcion buscar_ubicacion
    """
    lista = [{"latitude": "37.77", "longitude": "-122.42"},
             {"latitude": "37.78", "longitude": "-122.43"}]

    assert buscar_ubicacion(lista) == {"lat": [37.77, 37.78],"lon": [-122.42, -122.43]}