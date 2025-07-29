# Função que recebe um número variável de argumentos nomeados e retorna um dicionário com esses argumentos.

def mostrar_dados (**kwargs):
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")

    return kwargs

mostrar_dados(Nome= 'Yasmin Novais Vieira', Idade = 20)