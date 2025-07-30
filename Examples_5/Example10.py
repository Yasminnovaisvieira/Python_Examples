# Função que recebe um número variável de argumentos nomeados e retorna a média dos valores.

def media(**kwargs):
    numeros = []

    for valor in kwargs.values():
        try:
            numeros.append(float(valor))
        except ValueError:
            continue

    if len(numeros) == 0: # Verifica se a lista não está vazia
        print("Nenhum valor numérico foi fornecido.")
        return None

    soma = sum(numeros)
    media = soma / len(numeros)

    print(f"A média dos valores é: {media}")
    return media

entradas = {}

while True:
    try:
        quantidade = int(input("Digite a quantidade de categorias que deseja inserir: "))

        if quantidade > 0:
            break
        else:
            print("Digite um número inteiro positivo!")
    except ValueError:
        print("\nEntrada inválida. Digite um número inteiro.\n")

for i in range(quantidade):
    chave = input(f"Digite a {i + 1}ª categoria: ")
    valor = input(f"Digite o conteúdo de '{chave}': ")
    entradas[chave] = valor # Adiciona cada valor a sua determinada chave

media(**entradas)