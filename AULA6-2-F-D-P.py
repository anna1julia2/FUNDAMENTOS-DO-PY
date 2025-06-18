pares = 0
impares = 0
numero =int(input('digite um numero ou 0 para parar: '))
while numero != 0:
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
    numero = int(input('digite um numero ou 0 para parar: ' ))
    print('pares: ', pares, 'impares:', impares)
    