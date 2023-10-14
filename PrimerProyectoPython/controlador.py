import random
import requests
import json


class ControladorPokemon:
    NombrePokemon = ""

    # Constructor vacío
    def __init__(self):
        pass

    # Definicion funcion
    def comprobarNombrePokemon(self, pokemonUsu):
        if pokemonUsu == self.NombrePokemon:
            return True
        else:
            return False

    def generarPokemonAleatorio(self):
        # Número aleatorio que será el id del pokemon a adivinar
        aleatorioID = random.randint(1, 20)

        print(aleatorioID)

        # Llamada a la API
        pruebaDirecta = requests.get(
            f"https://pokeapi.co/api/v2/pokemon-form/{aleatorioID}/"
        )

        # JSON a dictionario si API responde
        if pruebaDirecta.status_code == 200:
            json_diccionario = json.loads(pruebaDirecta.text)
            self.NombrePokemon = json_diccionario["name"]
            print(self.NombrePokemon)

        else:
            print("La API no responde correctamente " + pruebaDirecta)
