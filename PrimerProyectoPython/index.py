import random
import requests
import json


# Definicion funcion
def adivinar(nombreAdivinar):
    respuestaUsu = input("¿Qué pokemon es?")

    if nombreAdivinar == respuestaUsu:
        print("Win")
    else:
        print("Loser")


# Número aleatorio que será el id del pokemon a adivinar
aleatorioID = random.randint(1, 20)

print(aleatorioID)

# Llamada a la API
pruebaDirecta = requests.get(f"https://pokeapi.co/api/v2/pokemon-form/{aleatorioID}/")

# JSON a dictionario si API responde
if pruebaDirecta.status_code == 200:
    json_diccionario = json.loads(pruebaDirecta.text)
    # print(json_diccionario)
    nombrePokemon = json_diccionario["name"]
    print(nombrePokemon)
    adivinar(nombrePokemon)

else:
    print("La API no responde correctamente " + pruebaDirecta)
