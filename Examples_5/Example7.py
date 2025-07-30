# Função que recebe um número variável de argumentos posicionais e nomeados e retorna a concatenação de todos eles.

def concatenar(*args, **kwargs):
    string = "".join(args)

    for chave, valor in kwargs.items():
        string += f"{chave}{valor}"

    print(f"\nResultado da concatenação: {string}")
    return string

contador = 0
entradas = {}
lista = []

print("Caso queira parar, digite 'PARAR'\n")

while True:
    while True:
        posicionais = input(f"Digite o {contador + 1}º argumento posicional: ")
        if posicionais.upper().strip() != 'PARAR':
            lista.append(posicionais)
            contador += 1

        elif posicionais.upper().strip() == 'PARAR':
            break

    while True:
        escolha = input("\nVocê deseja inserir argumentos nomeados? (S/N): ")

        if escolha.upper().strip() == 'S':
            quantidade = int(input("Digite a quantidade de categorias que deseja inserir: "))

            for i in range(quantidade):
                chave = input(f"Digite a {i + 1}ª categoria: ")
                valor = input(f"Digite o conteúdo de {chave}': ")
                entradas[chave] = valor

            break
        elif escolha.upper().strip() == 'N':
            break
        else:
            print("Digite 'S' ou 'N'!")

    break

concatenar(*lista, **entradas)