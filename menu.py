from termcolor import cprint


def mostrar_menu():
    cprint('--Pokedex--', 'red', attrs=['bold', 'blink'])
    cprint('1.Agregar Pokemon', 'green')
    cprint('2.Ver informacion de Pokemon', 'green')
    cprint('3.Editar Pokemon', 'green')
    cprint('4.Eliminar Pokemon', 'green')
    print()
    cprint('0. Salir','yellow', attrs=['bold'])
   
