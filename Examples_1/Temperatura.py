# Conversor de temperatura de Celsius para Fahrenheit e vice-versa.

escolha = int(input("Analisando as opções:\n1 - Graus Celsius para Fahrenheit.\n2 - Graus Fahrenheit para Celsius\nInsira a sua escolha:"))

if escolha == 1:
    grau_celsius = float(input("Digite em graus Celsius: "))
    grau_fahrenheit = (grau_celsius * 9 / 5) + 32
    print(f"{grau_celsius} Celsius é igual a {grau_fahrenheit} Fahrenheit.")
elif escolha == 2:
    grau_fahrenheit = float(input("Digite em graus Fahrenheit: "))
    grau_celsius = (grau_fahrenheit - 32) * 5 / 9
    print(f"{grau_fahrenheit} Fahrenheit é igual a {grau_celsius} Celsius.")
else:
    print("Escolha entre: 1 OU 2!")