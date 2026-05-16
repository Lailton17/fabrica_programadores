# Autor: Lailton Gomes
# Projeto: Desvio condicional 7

# Crição das variáveis
nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
cidade = input('Digite sua cidade: ')

if idade >= 12:
    print(f'Você é adolescente!')
elif idade >= 18:
    print(f'Você é adulto!')
else:
    print(f'Você é criança!')
