# Autor: Lailton Gomes
# Projeto: Atividade 2 loop while

n1 = int(input('Digite o número para a sua tabuada: '))
n2 = int(input('Digite o início da tabuada: '))
n3 = int(input('Digite o fim da tabuada: '))

# Loop WHILE
i = n2

while i <= n3:
    print(f'{n1} x {i} = {n1 * i}')
    i = i + 1