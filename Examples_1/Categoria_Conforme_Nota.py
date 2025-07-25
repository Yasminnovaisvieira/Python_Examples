# Solicita a nota do usuário e imprime qual categoria se encaixa

nota = float(input("Digite a sua nota: "))

if nota >= 9.0:
    print("Excelente.")
elif nota >= 7.0:
    print ("Boa.")
elif nota >=5.0:
    print ("Média.")
else:
    print ("Insuficiente.")