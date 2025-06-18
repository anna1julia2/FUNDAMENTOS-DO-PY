valor = float(input('valor da compra'))
if valor <= 100:
    desconto = 0
elif valor <= 500:
    desconto = 0.5
elif valor <= 1000:
    desconto = 0.10
else:
    desconto = 0.15
valor_final = valor * (1 - desconto)
print (f'valor com desconto: $ {valor_final:.2f}')

