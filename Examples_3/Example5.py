# Criar arquivo .XLSX

import pandas as pd

df = pd.DataFrame({
    "Produto":["Celular"],
    "Quantidade":[10]
})
df.to_excel("vendas.xlsx", index=False)

df = pd.read_excel("vendas.xlsx")
print(df)

