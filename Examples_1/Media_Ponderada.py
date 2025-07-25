n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))

peso1 = int(input("Digite o primeiro peso: "))
peso2 = int(input("Digite o segundo peso: "))
peso3 = int(input("Digite o terceiro peso: "))

media_ponderada = (n1*peso1 + n2*peso2 + n3*peso3) / (peso1+peso2+peso3)

print(f"O resultado da média ponderada é: {media_ponderada}")