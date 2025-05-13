import os
import json
from models.pokemon import Pokemon
from models.pokemon_comun import PokemonComun
from models.pokemon_legendario import PokemonLegendario
from models.pokemon_raro import PokemonRaro 
from utils.constants import FILE_NAME

def clear_console():
    if os.name == 'nt': 
        os.system('cls')  # Windows
    else:
        os.system('clear')  # Linux - Mac

def cargar_pokemon():
    try:
        with open(FILE_NAME, 'r') as file:
            data = json.load(file)
            pokemon_list = []
            for pokemon_data in data:
                categoria = pokemon_data.get('categoria')
                
                # Asegúrate de crear la instancia correcta basada en la categoría
                if categoria == 'Comun':
                    pokemon_list.append(PokemonComun.from_dict(pokemon_data))
                elif categoria == 'Raro':
                    pokemon_list.append(PokemonRaro.from_dict(pokemon_data))
                elif categoria == 'Legendario':
                    pokemon_list.append(PokemonLegendario.from_dict(pokemon_data))
                else:
                    print(f"Categoría desconocida para el Pokémon: {pokemon_data}")
            return pokemon_list
    except FileNotFoundError:
        return []

def guardar_pokemon(pokemon_db):
    with open(FILE_NAME, 'w') as file:
        json.dump([pokemon.to_dict() for pokemon in pokemon_db], file, indent=4)