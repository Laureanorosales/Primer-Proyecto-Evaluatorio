import os 


def clear_console():
    if os.name == 'nt': 
        os.system('cls') #Windows
    else:
        os.system('clear')  #Linux - Mac

