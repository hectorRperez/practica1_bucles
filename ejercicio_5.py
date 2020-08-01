if __name__ == "__main__":
    amount = float(input('Ingrese la cantidad a invertir: '))
    interest = float(input('Ingrese el interes anual: '))
    years = int(input('Ingrese la cantidad de años: '))

    for i in range(years):
        amount *= 1 + interest / 100
        print('Capital obtenido el ',i+1,'° años = ',round(amount,2))