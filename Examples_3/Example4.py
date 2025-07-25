# Criar arquivo .XML

xml_str = """<?xml version="1.0" enconding="UTF-8"?>
<config>
    <versao>1.0</versao>
</config>"""

with open("config.xml", "w", encoding="utf-8") as f:
    f.write(xml_str)

with open("config.xml", "r", encoding="utf-8") as f:
    conteudo = f.read()
    print(conteudo)