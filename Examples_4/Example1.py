# Função chamada "mostrar_hora" que imprime a hora atual do sistema.

import datetime

def mostrar_hora():
    agora = datetime.datetime.now()
    print(f"Horário Atual: {agora}")

mostrar_hora()