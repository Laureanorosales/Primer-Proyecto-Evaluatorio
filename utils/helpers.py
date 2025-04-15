import os, json

from models.pokemon import Pokemon
from utils.constants import FILE_NAME
from data.pokedex import pokemon_db



def clear_console():
    if os.name == 'nt': 
        os.system('cls') #Windows
    else:
        os.system('clear')  #Linux - Mac

def cargar_pokemon():
    try:
        with open(FILE_NAME, 'r') as file:
            data = json.load(file)
            return [Pokemon.from_dict(pokemon) for pokemon in data]
    except FileNotFoundError:
        return[]
    
def guardar_pokemon(pokemon_db):
    with open(FILE_NAME, 'w') as file:
        json.dump([pokemon.to_dict() for pokemon in pokemon_db], file, indent = 4)