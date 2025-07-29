# Função que recebe um número variável de argumentos posicionais e retorna a soma de todos eles.

def soma (*args):
    resultado = 0

    for arg in args:
        resultado += arg

    print(f"A soma de todos os Args é igual a: {resultado}")

lista_entrada = []

while True: # Repete enquanto o usuário digita números
    numero = input("Digite um valor: ")
    if numero.isnumeric(): # Verifica se a String é numérica
        lista_entrada.append(int(numero))
    else:
        break

print(soma(*lista_entrada)) # Desempacota a lista e roda a função soma() com os seus argumentos