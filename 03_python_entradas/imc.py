# Autor: Lailton Sousa
# Projeto: IMC em python

# Declarando variáveis
nome = input('Digite seu nome: ')
altura = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))
imc = peso / (altura * altura)

# print com f-string
print(f"Digite seu nome: {nome}")
print(f"Digite sua altura: {altura}")
print(f"Digite seu peso: {peso}")
print(f"Seu IMC é: {imc}")