# Função que recebe um número variável de argumentos posicionais e retorna o maior deles.

def maior_numero(*args):
    maior = max(lista)
    return maior

lista = []

print("Caso queira parar, digite 'N'\n")

while True:
    numero = input("Digite um número: ")
    if numero.strip().upper() == "N":
        break

    try:
        valor = float(numero)
        lista.append(valor)
    except ValueError:
        print("\nValor inválido. Digite um número ou 'N' para sair.\n")

print(f"\nO maior número digitado foi: {maior_numero(lista)}")