# Função que recebe uma lista de palavras como parâmetro e retorne a quantidade de palavras que começam com a letra "a".

def verificar_palavras(lista_palavras):
    contador = 0

    for palavra in lista_palavras:
        if palavra[0] == 'a' or palavra[0] == 'A':
            contador += 1

    print(f"A quantidade de palavras que começam com a letra 'A' é: {contador}")

    return contador



lista_palavras = ["amor", "feijão", "ARROZ"]

verificar_palavras(lista_palavras)