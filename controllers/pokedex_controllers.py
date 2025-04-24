from data.pokedex import pokemon_db
from utils.constants import CHECK, CROSS
from models.pokemon import Pokemon, PokemonComun, PokemonLegendario, PokemonRaro
from utils.helpers import cargar_pokemon, guardar_pokemon

# Pokemon
# Nombre - str
# Nivel - int
# Tipo - str
# Pequeña informacion - str
pokemon_db = cargar_pokemon()

# Funciones del Menu


def add_pokemon():
    nombre = input('Nombre del Pokemon: ')
    while True:
        try:
            nivel = int(input('Nivel: '))
            if nivel < 1:
                print('El nivel debe ser 1 o mayor.')
                continue
            break
        except ValueError:
            print('Ingresa un numero valido.')

    tipo = input('Tipo: ')
    info = input('Pequeña descripcion: ')
    
    # Solicitar categoría
    categoria = input("Categoría (Comun, Raro, Legendario): ").lower()

    if categoria == 'comun':
        nuevo_pokemon = PokemonComun(nombre, nivel, tipo, info)
    elif categoria == 'raro':
        rareza = input("Rareza: ")
        nuevo_pokemon = PokemonRaro(nombre, nivel, tipo, info, rareza, "")
    elif categoria == 'legendario':
        poder_especial = input("Poder especial: ")
        nuevo_pokemon = PokemonLegendario(nombre, nivel, tipo, info, poder_especial)
    else:
        print("Categoría no válida.")
        return

    pokemon_db.append(nuevo_pokemon)
    guardar_pokemon(pokemon_db)

    print(f'{nombre} fue agregado a la Pokedex con éxito.')


def list_pokemon():
    if not pokemon_db:
        print('No hay pokemones en la Pokedex!')
        return
    
    for index, pokemon in enumerate(pokemon_db, start=1):
        print(f"{index}. {pokemon.get_nombre()}")

    try:
        seleccion = int(input("Selecciona el número del Pokémon para ver sus detalles: "))
        
        if 1 <= seleccion <= len(pokemon_db):
            pokemon_seleccionado = pokemon_db[seleccion - 1]
            
           
            print("\n=== Detalles del Pokémon ===")
            print(f"Nombre: {pokemon_seleccionado.get_nombre()}")
            print(f"Nivel: {pokemon_seleccionado.get_nivel()}")
            print(f"Tipo: {pokemon_seleccionado.get_tipo()}")
            print(f"Descripción: {pokemon_seleccionado.get_info()}")
            
           
            if isinstance(pokemon_seleccionado, PokemonComun):
                print(f"Categoría: Común")
            elif isinstance(pokemon_seleccionado, PokemonRaro):
                print(f"Categoría: Raro")
                print(f"Rareza: {pokemon_seleccionado.get_rareza()}")
            elif isinstance(pokemon_seleccionado, PokemonLegendario):
                print(f"Categoría: Legendario")
                print(f"Poder Especial: {pokemon_seleccionado.get_poder_especial()}")
        else:
            print("Número fuera de rango.")
    
    except ValueError:
        print("Por favor, ingresa un número válido.")


def update_pokemon():
    if not pokemon_db:
        print('No hay pokemones para editar.')
        return

    list_pokemon()
    try:
        index = int(input('Selecciona el numero del Pokemon que quieres editar: ')) - 1
        if index < 0 or index >= len(pokemon_db):
            print('Número inválido')
            return
    except ValueError:
        print('Entrada inválida')
        return

    pokemon = pokemon_db[index]
    print(f"Editando a {pokemon.get_nombre()}...")

    nuevo_nombre = input(f"Nuevo nombre de [{pokemon.get_nombre()}]: ") or pokemon.get_nombre()
    nuevo_nivel = input(f"Nuevo nivel de [{pokemon.get_nivel()}]: ") or pokemon.get_nivel()
    nuevo_tipo = input(f"Nuevo tipo de [{pokemon.get_tipo()}]: ") or pokemon.get_tipo()
    nueva_info = input(f"Nuevo info de [{pokemon.get_info()}]: ") or pokemon.get_info()

    pokemon.set_nombre(nuevo_nombre)
    pokemon.set_nivel(int(nuevo_nivel))
    pokemon.set_tipo(nuevo_tipo)
    pokemon.set_info(nueva_info)

    
    if isinstance(pokemon, PokemonRaro):
        nueva_rareza = input(f"Nuevo rareza de [{pokemon.get_rareza()}]: ") or pokemon.get_rareza()
        pokemon.__dict__['_PokemonRaro__rareza'] = nueva_rareza  

    elif isinstance(pokemon, PokemonLegendario):
        nuevo_poder_especial = input(f"Nuevo poder especial de [{pokemon.get_poder_especial()}]: ") or pokemon.get_poder_especial()
        pokemon.__dict__['_PokemonLegendario__poder_especial'] = nuevo_poder_especial  

    guardar_pokemon(pokemon_db)

    print(f'Pokemon actualizado correctamente ✅')



def delete_pokemon():
    if not pokemon_db:
        print('No hay pokemones para eliminar')
        return

    list_pokemon()
    try:
        index = int(input('Selecciona el numero del pokemon que quieras eliminar: ')) - 1
        if index < 0 or index >= len(pokemon_db):
            print('Número inválido.')
            return
    except ValueError:
        print('Entrada inválida')
        return

    pokemon = pokemon_db[index]
    confirm = input(f"¿Estás seguro que quieres eliminar a {pokemon.get_nombre()}? (s/n): ").lower()

    if confirm == 's':
        
        if isinstance(pokemon, PokemonComun):
            print(f"Categoría: Común")
        elif isinstance(pokemon, PokemonRaro):
            print(f"Categoría: Raro - Rareza: {pokemon.get_rareza()}")
        elif isinstance(pokemon, PokemonLegendario):
            print(f"Categoría: Legendario - Poder Especial: {pokemon.get_poder_especial()}")

        eliminado = pokemon_db.pop(index)
        guardar_pokemon(pokemon_db)
        print(f"{eliminado.get_nombre()} fue eliminado con éxito de la Pokedex.")
    else:
        print('Eliminación cancelada')