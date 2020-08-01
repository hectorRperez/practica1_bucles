if __name__ == "__main__":
    number = int(input('Ingrese un número positivo: '))

    for i in range(1,number+1):
        
        if i == number:
            print('')
        elif i % 2 != 0:
                print(i,end=',')