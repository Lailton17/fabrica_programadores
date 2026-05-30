# Autor: Lailton Gomes
# Projeto: Tabuada com loop FOR (2)

# F-string 
numero = int(input('Digite o número para a sua tabuada: '))

for i in range (1,11):
    print(f'{numero} x {i} = {i * numero}')