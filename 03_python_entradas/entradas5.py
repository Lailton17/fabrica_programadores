# Autor: Lailton Sousa
# Projeto: Entradas com nomes e diferentes operações

# variáveis
nome = input('Digite seu nome: ')
valor1 = int(input('Digite o primeiro valor: '))
valor2 = int(input('Digite o segundo valor: '))
soma = valor1 + valor2 
multiplicacao = valor1 * valor2
subtracao = valor1 - valor2
divisao = valor1 / valor2

# print com f-string
print(f"Digite seu nome: {nome}")
print(f"O resultado da soma é: {soma}")
print(f"O resultado da multiplicação é: {multiplicacao}")
print(f"O resultado da subtração é: {subtracao}")
print(f"O resultado da divisão é: {divisao}")