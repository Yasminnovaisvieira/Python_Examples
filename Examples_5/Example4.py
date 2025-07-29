# Função que recebe um número variável de argumentos nomeados e retorna um dicionário com esses argumentos.

def mostrar_dados (**kwargs):
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")

    return kwargs

dados = {}

while True:
    entrada = input("Digite no formato chave:valor (ou qualquer outra coisa para parar): ")

    if ':' in entrada:
        chave, valor = entrada.split(':', 1) # Sep = Qual caractere será o "Separador" | Maxsplit = Define quantas vezes será dividida a String.
        dados[chave.strip()] = valor.strip()
    else:
        break

mostrar_dados(**dados)