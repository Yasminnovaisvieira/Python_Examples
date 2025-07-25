# Solicita um número e verificar se é par ou ímpar e se ele é múltiplo de 3 ou de 5.

numero = int(input("Digite um número: "))

if numero % 2 == 0:
    print(f"{numero} é PAR!")
else:
    print(f"{numero} é ÍMPAR!")

if numero % 3 == 0:
    print(f"{numero} é múltiplo por 3!")
elif numero % 5 == 0:
    print(f"{numero} é múltiplo por 5!")
else:
    print(f"{numero} não é múltiplo de 3 e 5!")