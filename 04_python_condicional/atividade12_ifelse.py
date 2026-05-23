# Autor: Lailton Gomes
# Projeto: Desvio Condicional 12

nome = input('Digite seu nome: ')
telefone = float(input('Digite seu telefone: '))
cidade = input('Digite o nome da sua cidade: ')
salario = float(input('Digite seu salário: '))


# Condições com f-string
if salario <= 5000:
    print(f'{nome}, você tem uma renda boa!')
if salario <= 1000:
    print(f'{nome}, você possui uma renda razoável!')
elif salario <= 700:
    print(f'{nome}, você possui uma renda baixa!')
elif salario <= 500:
    print(f'{nome}, você possui uma renda muito baixa!')
else:
    print(f'{nome}, você possui uma renda muito boa!')
