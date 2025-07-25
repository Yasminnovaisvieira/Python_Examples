# Função que recebe lista como parâmetro e retorna o maior item da lista.

def maior_numero(lista_numeros):
    maior_numero = lista_numeros[0]

    for numero in lista_numeros:
        if numero > maior_numero:
            maior_numero = numero

    print(f"\nO maior número da lista é: {maior_numero}")

    return maior_numero

tamanho_lista = int(input("Digite o tamanho da lista: "))
lista_numeros = []

for numero_lista in range(0, tamanho_lista):
    numero = int(input( f"Digite o {numero_lista + 1}º número da lista: "))

    lista_numeros.append(numero)

lista_numeros = maior_numero(lista_numeros)
