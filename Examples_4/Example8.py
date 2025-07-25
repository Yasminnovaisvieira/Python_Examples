# Função que recebe uma lista de números como parâmetro e retorna a média aritmética dos elementos.

def calcular_media(lista_numeros):
    contador = 0

    for numero in lista_numeros:
        soma_numeros =+ numero
        contador += 1

    media_numeros = soma_numeros / contador

    print(f"\nA média dos números da lista é: {media_numeros:.2f}")

    return media_numeros

tamanho_lista = int(input("Digite o tamanho da lista desejado: "))
lista_numeros = []

for numero_lista in range (0, tamanho_lista):
    numero = int(input( f"Digite o {numero_lista + 1}º número da lista: "))

    lista_numeros.append(numero)

calcular_media(lista_numeros)