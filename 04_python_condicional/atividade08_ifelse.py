# Autor: Lailton Gomes
# Projeto: Desvio condicional 8

# Crição das variáveis
nome = input('Digite seu nome: ')
salario = float(input('Digite seu salário: '))
valor = salario * 0.10

if valor >= 100:
    print(f'Você tem dinheiro')
else:
    print(f'Você não tem dinheiro')

