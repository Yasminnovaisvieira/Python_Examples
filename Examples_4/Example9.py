# Função que recebe uma lista de palavras como parâmetro e retorne a quantidade de palavras que começam com a letra "a".

def verificar_palavras(lista_palavras):
    contador = 0

    for palavra in lista_palavras:
        if palavra[0] == 'a' or palavra[0] == 'A':
            contador += 1

    print(f"\nA quantidade de palavras que começam com a letra 'A' é: {contador}")

    return contador


tamanho_lista = int(input("Digite o tamanho da lista: "))
lista_palavras = []

for palavra_lista in range(0, tamanho_lista):
    palavra_lista = str(input( f"Digite a {palavra_lista + 1}ª palavra da lista: "))

    lista_palavras.append(palavra_lista)

verificar_palavras(lista_palavras)