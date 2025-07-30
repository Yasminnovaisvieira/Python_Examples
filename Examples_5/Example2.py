# Função que recebe um número variável de argumentos posicionais e retorna a soma de todos eles.

def soma (*args):
    resultado = 0

    for arg in args:
        resultado += arg

    print(f"\nA soma de todos os Args é igual a: {resultado:.2f}")

    return resultado

lista_entrada = []

while True: # Repete enquanto o usuário digita números
    numero = input("Digite um valor: ")

    try:
        valor = float(numero)
        lista_entrada.append(valor)
    except ValueError:
        break

soma(*lista_entrada) # Desempacota a lista e roda a função soma() com os seus argumentos