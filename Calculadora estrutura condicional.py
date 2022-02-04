total = 0
print('******************************Calculadora python**********************************')
print(' Digite 1 - SOMA')
print(' Digite 2 - SUBTRAÇÃO')
print(' Digite 3 - DIVISÃO')
print(' Digite 4 - MULTIPLICACAO')
valor = input('Escolha a opcao de operacao')
valor1 = input('Entre o com primeiro numero da operacao')
valor2 = input('Entre com o segundo numero da operacao')
if valor == '1':
    total = int(valor1) + int(valor2)
    print(total)
elif valor == '2':
    total = int(valor1) - int(valor2)
    print(total)
elif valor == '3':
    total = int(valor1) / int(valor2)
    print(total)
elif valor == '4':
    total = int(valor1) * int(valor2)
    print(total)
else:
    print('valor digitado nao pertence a nenhuma operacao')







