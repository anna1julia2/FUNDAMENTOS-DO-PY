dia = int(input("Dia: "))
mes = int(input("Mês: "))
ano = int(input("Ano: "))
bissexto = (ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0))
dias_mes = [31, 29 if bissexto else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if 1 <= mes <= 12 and 1 <= dia <= dias_mes[mes - 1]:
    print("Data válida")
else:
    print("Data inválida")