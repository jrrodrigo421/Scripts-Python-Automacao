print('******************************Calculadora python**********************************')
def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def divide(x, y):
    return x / y
def multiply(x, y):
    return x * y
print(' Digite 1 - SOMA')
print(' Digite 2 - SUBTRAÇÃO')
print(' Digite 3 - DIVISÃO')
print(' Digite 4 - MULTIPLICACAO')
valor = input('Escolha a opcao de operacao')
valor1 = int(input('Entre o com primeiro numero da operacao'))
valor2 = int(input('Entre com o segundo numero da operacao'))
if valor == '1':
    print(add(valor1, valor2))
    print = input('Deseja fazer outra operacao (S / N) ?? ')
elif valor == '2':
    print(subtract(valor1, valor2))
    print = input('Deseja fazer outra operacao (S / N) ?? ')
elif valor == '3':
    print(divide(valor1, valor2))
    print = input('Deseja fazer outra operacao (S / N) ?? ')
elif valor == '4':
    print(multiply(valor1, valor2))
    print = input('Deseja fazer outra operacao (S / N) ?? ')
else:
    print('valor digitado nao pertence a nenhuma operacao')
    exit()




