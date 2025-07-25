# Função que recebe uma string e um caractere como parâmetros e retorna o número de vezes que o caractere aparece na string.

def quantidade_caractere(texto, caractere):
    contador = 0

    for letra in texto:
        if letra.lower() == caractere.lower():
            contador += 1

    print(f"A quantidade de vezes que {caractere} aparece no texto '{texto}' é: {contador}")

    return contador

texto = str(input("Digite um texto: "))
caractere = str(input("Digite o caractere que deseja quantas vezes está presente nesse texto: "))

quantidade_caractere(texto, caractere)