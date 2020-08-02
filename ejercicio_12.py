if __name__ == "__main__":
    word = input('Ingrese una frase: ')
    letra = input('Ingrese una letra: ')

    contador = 0
    for i in word:
        if i == letra:
            contador +=1
    
    print('La letra {} aparece en la palabra {} {} veces '.format(letra, word, contador))
