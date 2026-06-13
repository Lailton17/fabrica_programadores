# Autor: Lailton Gomes
# Projeto: Listas em Python

# Contatos salvos
#            0          1         2         3
nomes = ['Lailton', 'Kemilly', 'Laiani', 'Hester']
print(*nomes)

# Adicionar um novo contato
nomes.append('Gabryell')
print(*nomes)

# Deletar um contato
del nomes[2]
print(*nomes)

# Encerrar o programa
nomes.clear()
print(f'Após o encerramento, a lista é: {nomes}')