# Autor: Lailton Gomes
# Projeto: Desvio condicional 9

# Crição das variáveis
nome = input('Digite seu nome: ')
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura * altura)

if imc <= 18.5:
    print(f'Você é magro')
else:
    print(f'Você está no peso normal')

    
