# Autor: Lailton Gomes
# Projeto: Atividade 4 loop FOR (variáveis de início e fim)

# F-string 
n1 = int(input('Digite o número para a sua tabuada: '))
n2 = int(input('Digite o início da tabuada: '))
n3 = int(input('Digite o fim da tabuada: '))

# Loop FOR
for i in range (n2, n3 + 1):
    print(f'{n1} x {i} = {i * n1}')
