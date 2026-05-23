# Autor: Lailton Gomes
# Projeto: Desvio condicional 9

# Crição das variáveis
nome = input('Digite seu nome: ')
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura * altura)

if imc <= 18.5:
    print(f'Você está magro!')
elif imc <= 24.9:
    print(f'Você está no peso normal!')
elif imc <= 29.9:
    print(f'Você está no estado de sobrepeso!')
elif imc <= 39.9:
    print(f'Você está em estado de obesidade!')
else:
    print(f'Você está em estado de obesidade grave!')

