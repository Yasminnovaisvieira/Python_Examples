# Função que recebe um número variável de argumentos posicionais e retorna a soma de todos eles.

def soma (*args):
    numeros_somados = 0

    for arg in args:
        numeros_somados += arg

    print(f"A soma de todos os Args é igual a: {numeros_somados}")

soma(2,4,5,6)