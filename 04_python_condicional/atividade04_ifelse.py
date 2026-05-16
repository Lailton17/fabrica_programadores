# Autor: Lailton Gomes
# Projeto: Desvio Condicional 4

# Criação das variáveis
nome = input('Digite seu nome: ')
idade = int(input('Digite a sua idade: '))
cnh = input('Possui cnh?: ')

if idade >= 18 and cnh == 'Sim' :
    print(f'{nome}, você pode dirigir')
else:
    print(f'{nome}, você não pode dirigir')
