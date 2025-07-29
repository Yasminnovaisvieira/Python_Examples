# Função que recebe um número variável de argumentos nomeados e retorna um dicionário com esses argumentos.

def criar_dicionario(**kwargs): # Dentro dessa função, kwargs é considerado dicionário
    return kwargs # Kwargs será um dicionário com os argumentos passados

entradas = {}

# Quantos pares {chave}:{valor} o usuário deseja inserir
quantidade = int(input("Digite a quantidade de categorias que você deseja inserir: "))

for i in range(quantidade):
    chave = input(f"Digite a {i+1}ª categoria: ")
    valor = input(f"Digite o conteúdo de '{chave}': ")
    entradas[chave] = valor  # Adiciona ao dicionário o valor referente a chave específica

print("\nDicionário final: ") # Passando o dicionário como 'argumentos nomeados' usando **
print(criar_dicionario(**entradas))