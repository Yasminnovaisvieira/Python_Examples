# Criar arquivo .TXT.

with open("meu_arquivo.txt", "w") as arquivo:
    arquivo.write("Hello, World!\n")
    arquivo.write("I´m Yasmin Novais Vieira.\n")

''' ## Outra maneira ###
resultado = arquivo.read()
print(resultado)
'''

with open("meu_arquivo.txt", "r") as arquivo: # Caso o arquivo não esteja dentro do projeto, é preciso colocar o caminho no lugar
    arquivo = open("meu_arquivo.txt", "r")
    conteudo = arquivo.read()
    print(conteudo)
