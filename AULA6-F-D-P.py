maior = -99999999999999999999999999999999999999
numero = int(input('digite um numero ou -1 para parar: '))
while numero != -1:
    if numero > maior:
       maior = numero
    numero = int(input('digite um numero ou -1 para parar: '))
    print('o maior numero e: ', maior)
    