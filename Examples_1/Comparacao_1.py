# Solicita dois números ao usuário e verifica qual é o maior

numero1 = int(input("Digite o 1º número: "))
numero2 = int(input("Digite o 2º número: "))

if numero1 > numero2:
    print(f"{numero1} é MAIOR que {numero2}!")
elif numero1 < numero2:
    print(f"{numero2} é MAIOR que {numero1}!")
else:
    print("Os números são iguais.")