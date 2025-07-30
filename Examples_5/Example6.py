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

concatenar("Yas", "min", " ", Nova="is")