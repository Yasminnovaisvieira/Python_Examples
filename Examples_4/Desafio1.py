# Função que armazena os dados dos habitantes em uma lista de dicionários e calcula a idade média dos homens que gostam de natação, exibindo um aviso caso não haja nenhum.

def armazenar_informacoes():
    habitantes = [
        {"Nome" : "Yasmin", "Sexo" : "Feminino", "Esporte Favorito" : "Vôlei", "Idade" : 20},
        {"Nome": "Julya", "Sexo": "Feminino", "Esporte Favorito": "Natação", "Idade": 20},
        {"Nome": "André", "Sexo": "Masculino", "Esporte Favorito": "Futebol", "Idade": 19},
        {"Nome": "Antônio", "Sexo": "Masculino", "Esporte Favorito": "Tênis", "Idade": 17}
    ]

    return habitantes

def aviso_sem_homens_natacao():
    print("Entre os quatro habitantes não existem homens que gostam de natação.")

def calcular_idade_media_natacao(habitantes):
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

habitantes = armazenar_informacoes()
calcular_idade_media_natacao(habitantes)
