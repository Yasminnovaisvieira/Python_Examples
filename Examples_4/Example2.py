# Função "Mostrar Menu" que imprime um menu simples com algumas sugestões.

def mostrar_menu():
    print("========= MENU =========\n")

    print("1 - Ligar para Leonardo Oliveira")
    print("2 - Enviar mensagem para Leonardo Oliveira")
    print("3 - Localizar Leonardo Oliveira")

    escolha = int(input("\nDigite sua escolha: "))

    if escolha == 1:
        print("Ligando para Leonardo Oliveira...\n")
    elif escolha == 2:
        print("Enviando mensagem para Leonardo Oliveira...\n")
    elif escolha == 3:
        print("Localizando Leonardo Oliveira...\n")
    else:
        print("Escolha uma opção válida!\n")

    return encerrar()

def encerrar():
    sair = input("Deseja sair? [S/N]: ")

    if sair == "S":
        return "Saindo..."
    elif sair == "N":
        return mostrar_menu()
    else:
        print("Você digitou uma opção inexistente!")

mostrar_menu()