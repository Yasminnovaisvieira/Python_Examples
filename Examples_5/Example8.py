# Função que recebe um número variável de argumentos posicionais e retorna o maior deles.

def maior_numero(*args):
    maior = max(args)

    print(f"O maior número entre {lista} é: {maior}")

    return maior

lista = [5, 9.5, 22, 1000]

maior_numero(*lista)