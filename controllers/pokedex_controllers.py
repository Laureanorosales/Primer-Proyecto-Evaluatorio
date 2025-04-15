from data.pokedex import pokemon_db
from utils.constants import CHECK, CROSS
from models.pokemon import Pokemon
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
        #Manejo de error para que el nivel no sea negativo o menor que 1
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
    #Pokemon creado
    nuevo_pokemon = Pokemon(nombre, nivel, tipo, info)
    #Pokemon guardado en la db
    pokemon_db.append(nuevo_pokemon)
    guardar_pokemon(pokemon_db)

    print(f'{nombre} fue agregado a la pokedex con éxito.')

def list_pokemon():
    if not pokemon_db:
        print('No hay pokemones en la Pokedex!')
        return
    for index, pokemon in enumerate(pokemon_db, start=1):
        print(f"{index}. {pokemon.nombre}")  

    try:
        seleccion = int(input("Selecciona el número del Pokémon para ver sus detalles: "))
        if 1 <= seleccion <= len(pokemon_db):
            pokemon_seleccionado = pokemon_db[seleccion - 1]
            print("\n=== Detalles del Pokémon ===")
            print(f"Nombre: {pokemon_seleccionado.nombre}")
            print(f"Nivel: {pokemon_seleccionado.nivel}")
            print(f"Tipo: {pokemon_seleccionado.tipo}")
            print(f"Descripción: {pokemon_seleccionado.info}")
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
            print('Numero invalido')
            return
    except ValueError:
        print('Entrada invalida')
        return

    pokemon = pokemon_db[index]
    print(f"Editando a {pokemon.nombre}...")

    nuevo_nombre = input(f"Nuevo nombre de [{pokemon.nombre}]: ") or pokemon.nombre
    nuevo_nivel = input(f"Nuevo nivel de [{pokemon.nivel}]: ") or pokemon.nivel
    nuevo_tipo = input(f"Nuevo tipo de [{pokemon.tipo}]: ") or pokemon.tipo
    nueva_info = input(f"Nuevo info de [{pokemon.info}]: ") or pokemon.info

    pokemon.nombre = nuevo_nombre
    pokemon.nivel = int(nuevo_nivel)
    pokemon.tipo = nuevo_tipo
    pokemon.info = nueva_info

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
            print('Numero Invalido.')
            return
    except ValueError:
        print('Entrada invalida')
        return

    pokemon = pokemon_db[index]
    confirm = input(f"¿Estas seguro que quieres eliminar a {pokemon.nombre}? (s/n): ").lower()
    if confirm == 's':
        eliminado = pokemon_db.pop(index)
        guardar_pokemon(pokemon_db)
        print(f"{eliminado.nombre} fue eliminado con exito de la Pokedex.")
    else:
        print('Eliminacion cancelada')
