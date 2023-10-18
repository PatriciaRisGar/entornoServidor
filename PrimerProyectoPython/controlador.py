import random
import requests
import json
from PIL import ImageTk
from urllib.request import urlopen


class ControladorPokemon:
    NombrePokemon = ""
    ImagenPokemon = None

    # Constructor vacío
    def __init__(self):
        pass

    # Definicion funcion
    def comprobarNombrePokemon(self, pokemonUsu):
        if pokemonUsu.lower() == self.NombrePokemon.lower():
            return True
        else:
            return False

    # Traer pokemon de la API
    def generarPokemonAleatorio(self):
        # Número aleatorio que será el id del pokemon a adivinar
        aleatorioID = random.randint(1, 20)

        # Llamada a la API
        datosPokemon = requests.get(
            f"https://pokeapi.co/api/v2/pokemon-form/{aleatorioID}/"
        )

        # JSON a dicionario si API responde
        if datosPokemon.status_code == 200:
            json_diccionario = json.loads(datosPokemon.text)
            self.NombrePokemon = json_diccionario["name"]
            self.ImagenPokemon = json_diccionario["sprites"]["front_default"]
            datos = urlopen(self.ImagenPokemon)
            imagenGUI = ImageTk.PhotoImage(data=datos.read())
            print(self.NombrePokemon)
            return imagenGUI

        else:
            print("La API no responde correctamente " + datosPokemon)
