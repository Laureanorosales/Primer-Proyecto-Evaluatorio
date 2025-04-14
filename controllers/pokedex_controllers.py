from data.pokedex import pokemon_db
from utils.constants import CHECK, CROSS
# Pokemon
# Nombre - str
# Nivel - int
# Tipo - str
# Pequeña informacion - str


def add_pokemon():
    nombre = input('Nombre del Pokemon: ')
    nivel = int(input('Nivel: '))
    tipo = input('Tipo: ')
    info = input('Pequeña descripcion: ')

    newPokemon = {
        'nombre': nombre,
        'nivel': nivel,
        'tipo': tipo,
        'info': info
    }

    pokemon_db.append(newPokemon)
    print(f'{nombre} fue agregado a la Pokedex con Exito {CHECK}')


def list_pokemon():
    if not pokemon_db:
        print('No hay pokemones en la Pokedex!')
        return
    for index, pokemon in enumerate(pokemon_db, start=1):
        print(f"{index}.{pokemon['nombre']}")

    try:
        seleccion = int(
            input("Selecciona el número del Pokémon para ver sus detalles: "))
        if 1 <= seleccion <= len(pokemon_db):
            pokemon_seleccionado = pokemon_db[seleccion - 1]
            print("\n=== Detalles del Pokémon ===")
            print(f"Nombre: {pokemon_seleccionado['nombre']}")
            print(f"Nivel: {pokemon_seleccionado['nivel']}")
            print(f"Tipo: {pokemon_seleccionado['tipo']}")
            print(f"Descripción: {pokemon_seleccionado['info']}")
        else:
            print("Número fuera de rango.")
    except ValueError:
        print("Por favor, ingresa un número válido.")


def update_pokemon():
    if not pokemon_db:
        print(' No hay pokemones para editar.')

    list_pokemon()
    try:
        index = int(
            input('Selecciona el numero del Pokemon que quieres editar: ')) - 1
        if index < 0 or index >= len(pokemon_db):
            print('Numero invalido')
            return
    except ValueError:
        print('Entrada invalida')
        return

    pokemon = pokemon_db[index]
    print(f"Editando a {pokemon['nombre']}...")

    nuevo_nombre = input(
        f"Nuevo nombre [{pokemon['nombre']}]") or pokemon['nombre']

    nuevo_nivel = input(
        f"Nuevo nivel [{pokemon['nivel']}]") or pokemon['nivel']

    nuevo_tipo = input(f"Nuevo tipo [{pokemon['tipo']}]") or pokemon['tipo']

    nueva_info = input(f"Nuevo info [{pokemon['info']}]") or pokemon['info']

    pokemon.update({
        'nombre': nuevo_nombre,
        'nivel': int(nuevo_nivel),
        'tipo': nuevo_tipo,
        'info': nueva_info
    })

    print(f'Pokemon actualizado correctamente {CHECK}')


def delete_pokemon():
    if not pokemon_db:
        print('No hay pokemones para eliminar')
        return

    list_pokemon()
    try:
        index = int(
            input('Selecciona el numero del pokemon que quieras eliminar: ')) - 1
        if index < 0 or index >= len(pokemon_db):
            print('Numero Invalido.')
            return
    except ValueError:
        print('Entrada invalida')
        return

    pokemon = pokemon_db[index]
    confirm = input(
        f"¿Estas seguro que quieres eliminar a {pokemon['nombre']}? (s/n): ").lower()
    if confirm == 's':
        eliminado = pokemon_db.pop(index)
        print(f"{eliminado['nombre']} fue eliminado con exito de la Pokedex.")
    else:
        print('Eliminacion cancelada')
