prestacao = float(input("Digite o valor da prestação: "))
juros = float(input("Digite a taxa dos juros: "))

valor_atrasado = prestacao + (prestacao * juros)

print(f"O valor da prestação em atraso é: {valor_atrasado}")