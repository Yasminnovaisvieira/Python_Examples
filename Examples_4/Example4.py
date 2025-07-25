# Função chamada "imprimir_triangulo" que imprime um triângulo formado por asteriscos.

def imprimir_triangulo(num_linhas):
    for linha in range(1, num_linhas + 1): # Para imprimir a quantidade de linhas correta
        print("*" * linha)

num_linhas = int(input("Digite sua quantidade de linhas: "))

imprimir_triangulo(num_linhas)