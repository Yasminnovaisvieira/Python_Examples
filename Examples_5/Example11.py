# Função que recebe um número variável de argumentos nomeados e retorna a média dos valores.

def media(**kwargs):
    numeros = []

    for valor in kwargs.values():
        try:
            numeros.append(float(valor))
        except ValueError:
            continue

    if len(numeros) == 0:
        print("Nenhum valor numérico foi fornecido.")
        return None

    soma = sum(numeros)
    media = soma / len(numeros)

    print(f"A média dos valores é: {media:.2f}")
    return media

entradas = {
    "1ª Categoria": "20.5",
    "2ª Categoria": "50",
    "3ª Categoria": "12.2",
    "4ª Categoria": "Teste"
}

media(**entradas)
