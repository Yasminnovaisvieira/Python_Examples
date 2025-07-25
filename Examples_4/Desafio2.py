# Função que armazena os dados dos habitantes em uma lista de dicionários e calcula a idade média dos homens que gostam de natação, exibindo um aviso caso não haja nenhum.

dados_habitante = []

def coletar_dados():
    for pessoa in range(1, 5):
        nome = input(f"Digite o nome da {pessoa}ª pessoa: ")
        sexo = input(f"Digite o sexo {pessoa}ª pessoa: ")
        esporte_favorito = input(f"Digite o esporte favorito da {pessoa}ª pessoa: ")
        idade = int(input(f"Digite a idade da {pessoa}ª pessoa: "))

        habitante = {
            "Nome" : nome,
            "Sexo" : sexo,
            "Esporte Favorito" : esporte_favorito,
            "Idade" : idade
        }

        dados_habitante.append(habitante)


def armazene_dados():
    habitantes = dados_habitante

    return habitantes


def aviso_sem_homens_natacao():
    print("Entre os quatro habitantes não existem homens que gostam de natação.")


def calcular_sem_homens_natacao(habitantes):
    idades_homens_natacao = []

    for pessoa in habitantes:
        if pessoa["Sexo"] == "Masculino" and pessoa["Esporte Favorito"] == "Natação":
            idades_homens_natacao.append(pessoa["Idade"])

    # Verifica se a lista não está vazia para evitar divisão por zero
    if idades_homens_natacao:
        media = sum(idades_homens_natacao) / len(idades_homens_natacao)
        print(f"A idade média dos homens que gostam de natação é: {media:.2f} anos.")
    else:
        aviso_sem_homens_natacao()


habitantes = armazene_dados()
calcular_sem_homens_natacao(habitantes)