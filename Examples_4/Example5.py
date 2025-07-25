# Função para soma com dois números como parâmetros

def soma (num1, num2):
    soma = num1 + num2

    print(f"\nO resultado da soma é: {soma:.2f}")
    return soma

num1 = float(input("Digite o 1º número: "))
num2 = float(input("Digite o 2º número: "))

soma(num1, num2)