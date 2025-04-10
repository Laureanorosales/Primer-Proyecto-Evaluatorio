from menu import mostrar_menu


def run():
    while True:
        mostrar_menu()
        option = input('Elije una opción [0-4]: ')
        match option:
            case '1':
                print('Opción 1 seleccionada')
            case '2':
                print('Opción 2 seleccionada')
            case '3':
                print('Opción 3 seleccionada')
            case '4':
                print('Opción 4 seleccionada')
            case '0':
                print('¡Hasta luego!')
                break
            case _:
                print('Opción inválida. Intenta de nuevo.')
                
if __name__ == "__main__":
    run()
