
from menu import mostrar_menu
from controllers.pokedex_controllers import add_pokemon, update_pokemon, list_pokemon, delete_pokemon
from utils.helpers import clear_console
from data.pokedex import pokemon_db


def run():
    clear_console()
    while True:
        mostrar_menu()
        option = input('Elije una opción [0-4]: ')
        clear_console()
        match option:
            case '1':
                add_pokemon()
            case '2':
                list_pokemon()
            case '3':
                update_pokemon()
            case '4':
                delete_pokemon()
            case '0':
                print('Saliendo...')
                break
            case _:
                print('Opción inválida. Intenta de nuevo.')


if __name__ == "__main__":
    run()
