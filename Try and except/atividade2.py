# Autor: Lailton Gomes
# Projeto: Calculadora com try e except

numero1 = input("Digite o primeiro número: ")
numero1 = input("Digite o segundo número: ")

try:
    numero1 = int(numero1)
    numero2 = int(numero2)
    print(numero1 + numero2)
except:
    print("Somente números são permitidos")
