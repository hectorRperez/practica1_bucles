from getpass import getpass

if __name__ == "__main__":
    password = 'contraseña'

    while True:
        key = getpass('Introduzca su contraseña: ')
        if key == password:
            print('Contraseña correcta')
            break
        else:
            print('Contraseña incorrecta')