# Autor: Lailton Gomes
# Projeto: Desvio Condicional (nota >= 7 aprovado, <= 4 reprovado)

# Criação das variáveis
nome = input('Digite seu nome: ')
nota = float(input('Digite a nota final: '))

if nota >= 7:
    print(f'{nome}, você está aprovado')
elif nota >= 5:
    print(f'{nome}, você está de recuperacão')
else:
    print(f'{nome}, você está reprovado')
