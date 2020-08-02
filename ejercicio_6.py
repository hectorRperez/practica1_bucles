if __name__ == "__main__":
    number = int(input('Ingrese un número entero positivo: '))

    for i in range(1,number+1):
        for j in range(i):
            print('*',end='')
        
        print(' ')