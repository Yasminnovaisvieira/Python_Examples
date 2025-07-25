# Criar arquivo .CSV

import csv

with open ("produtos.csv", "w", newline='') as csvfile: # Newline tira a quebra de linha automática
    csv.writer(csvfile, delimiter=',').writerow(['Livro', '19.90'])
    csv.writer(csvfile, delimiter=',').writerow(['Revista', '9.99'])
    csv.writer(csvfile, delimiter=',').writerow(['Jornal', '2.99'])

with open("produtos.csv", "r") as csvfile:
    for x in csv.reader(csvfile):
        print(x)

'''
with open ("produtos.csv", "w", newline="") as f: 
    writer = csv.writer(f)
    writer.writerow(["Moletom", "250.00"])
    writer.writerow(["Livro", "20.00"])

with open("produtos.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
'''