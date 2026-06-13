# Autor: Lailton Gomes
# Projeto: Listas em Python

#           0         1         2         3          4        5
nomes = ['Pelé', 'Maradona', 'Messi', 'Ronaldo'] # Neymar # Pedro (MBAPPÉ)
print(*nomes)

# adicionando um nome na lista
nomes.append('Pedro')
print(*nomes)

# adicionando um nome em uma posição específica
nomes.insert(4,'Neymar')
print(*nomes)

# modificando uma pessoa da lista
nomes[5] = 'Mbappé'
print(*nomes)

# Removendo um nome da lista
del nomes[2]
print(*nomes)

# removendo um nome por texto
# buscar um nome a apagar o primeiro que aparecer
nomes.remove('Maradona')
print(*nomes)

# usando o pop para mostrar o nome removido
#  0      1      2      3
# Pelé Ronaldo Neymar Mbappé
removido = nomes.pop(1)
print(f'Após o pop, foi removido o nome: {removido}', nomes)

# limpar a lista
nomes.clear()
print(f'Após o clear, a lista é: {nomes}')