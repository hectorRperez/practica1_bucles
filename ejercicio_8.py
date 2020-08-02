if __name__ == "__main__":
    number = int(input('Ingrese un número entero: '))

    for i in range(1,number+1,2):
        print('i: ',i)
        for j in range(i,0,-2):
            print(j,end=' ')
        
        print(' ')
