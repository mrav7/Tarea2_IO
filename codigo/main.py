import sys
import numpy as np


def main(argv=sys.argv) -> None:

  instancia = 0
  tamano_local = []

  #Lee el archivo con las instancias
  with open("instancias/QAP_sko56_04_n.txt") as Texto:

    # Obtengo la cantidad de instancias
    instancia = int(Texto.readline())

    # Obtengo la distancias de cada local
    dist = Texto.readline().split(",")

    for x in range(len(dist)):
      tamano_local.append(int(dist[x]))

    peso_flujo = np.empty((instancia, instancia), int)

    # Obtengo las distancias entre locales
    for i in range(0, instancia):
      data = Texto.readline().split(",")
      for j in range(len(data)):
        peso_flujo[i][j] = int(data[j])

  print(type(instancia))
