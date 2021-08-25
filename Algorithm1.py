from heapq import heappop, heappush


def mapa2graf(mapa):
    '''Función que lee el mapa y devuelve un diccionario con las posiciones
    disponibles que se pueden recorrer y su respectiva coordenada.'''
    alto = len(mapa)
    ancho = len(mapa[0]) if alto else 0
    graf = {(i, j): [] for j in range(ancho)
            for i in range(alto) if not mapa[i][j]}
    for fila, col in graf.keys():
        if fila < alto - 1 and not mapa[fila + 1][col]:
            graf[(fila, col)].append(("S", (fila + 1, col)))
            graf[(fila + 1, col)].append(("N", (fila, col)))
        if col < ancho - 1 and not mapa[fila][col + 1]:
            graf[(fila, col)].append(("E", (fila, col + 1)))
            graf[(fila, col + 1)].append(("O", (fila, col)))
    return graf


def heuristica(celda, objetivo):
    '''Función h'(n) que devuelve la distancia entre dos puntos.'''
    return abs(celda[0] - objetivo[0]) + abs(celda[1] - objetivo[1])


def Astar(mapa, posInit, posFin):
    '''Función que ejecuta el algoritmo A*'''
    inicio, objetivo = posInit, posFin

    # Se crea el elmento que serivirá para almacenar los nodos que se pueden
    # recorrer según la posición.
    cola_prior = []

    # Se agrega a la lista el nodo inicio que tiene costo cero.
    heappush(cola_prior, (0 + heuristica(inicio, objetivo), 0, "", inicio))
    # print(cola_prior)

    # Se crea la tupla que recibirá las posiciones ya visitadas junto con los
    # puntos cardinales.
    visitado = set()

    graf = mapa2graf(mapa)
    # print(graf)

    # Ciclo que se ejecuta hasta encontrar la ruta mas optima.
    while cola_prior:
        _, costo, ruta, actual = heappop(cola_prior)

        # Se verifica si la posición actual es la posición objetivo. Si lo es,
        # devuelve la ruta y termina el ciclo.
        if actual == objetivo:
            return ruta
        # Se verifica si la posición actual ya ha sido visitada. Si lo ha sido
        # continúa.
        if actual in visitado:
            continue

        # Lista cerrada donde se gurdan las posiciones ya visitadas.
        visitado.add(actual)

        # print(graf[actual])
        # Iteración que permite recorrer la ruta de menor costo hasta el
        # objetivo dependiendo del nodo en el que se encuentra.
        for direccion, vecinos in graf[actual]:
            # Se agregan a la lista la función de evaluación f(n), el costo de
            # llegar al nodo, la ruta recorrida y los nodos que ya se han
            # procesado y expandido.
            # Donde 'costo + heuristica(vecinos, objetivo)' = g(n) + h'(n) = f(n)
            heappush(cola_prior, (costo + heuristica(vecinos, objetivo),
                                  costo + 1, ruta + direccion, vecinos))

    return "NO WAY!"


def main():
    # Mapa original, sin elementos.
    mapa = [[1, 1, 1, 1, 1, 1],
            [1, 0, 1, 0, 0, 1],
            [1, 0, 1, 0, 0, 1],
            [1, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1]]

    print('   Mapa:')
    for i in range(len(mapa)):
        print('\t', mapa[i])

    # Posiciones iniciales de los elementos que interactúan.
    posI = {
        'R': (3, 3),
        'M3': (1, 4),
        'M2': (3, 1),
        'M1': (1, 1)
    }
    # Posiciones finales de los elementos. No se coloca posición final de R
    # porque es la misma que la posicion final de M1.
    posF = {
        'M3': (4, 2),
        'M2': (4, 3),
        'M1': (4, 4)
    }

    print('   Ruta encontrada:')
    # Mover R a M3 y luego llevarlo a su posición final.
    print('\t', 'Mover R a M3 - Ruta: ' + Astar(mapa, posI['R'], posI['M3']) + '\n'
          + '\t', 'Mover M3 a posF_M3 - Ruta: ' + Astar(mapa, posI['M3'], posF['M3']))

    # Mover R (que está en posición final de M3) a M2 y luego llevarlo a su
    # posición final.
    print('\t', 'Mover R a M2 - Ruta: ' + Astar(mapa, posF['M3'], posI['M2']) + '\n'
          + '\t', 'Mover M2 a posF_M2 - Ruta: ' + Astar(mapa, posI['M2'], posF['M2']))

    # Mover R (que está en posición final de M2) a M1 y luego llevarlo a su
    # posición final.
    print('\t', 'Mover R a M1 - Ruta: ' + Astar(mapa, posF['M2'], posI['M1']) + '\n'
          + '\t', 'Mover M1 a posF_M1 - Ruta: ' + Astar(mapa, posI['M1'], posF['M1']))
    return 0


if __name__ == '__main__':
    main()
