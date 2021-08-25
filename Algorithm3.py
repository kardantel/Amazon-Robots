from heapq import heappop, heappush


def maze2graph(maze):
    '''Función que lee el mapa y devuelve un diccionario con las posiciones
    disponibles que se pueden recorrer en cada nodo y su respectivo
    desplazamiento.'''
    height = len(maze)
    width = len(maze[0]) if height else 0
    graph = {(i, j): [] for j in range(width)
             for i in range(height) if not maze[i][j]}
    for row, col in graph.keys():
        if row < height - 1 and not maze[row + 1][col]:
            graph[(row, col)].append(("MoverAbajo-> ", (row + 1, col)))
            graph[(row + 1, col)].append(("MoverArriba-> ", (row, col)))
        if col < width - 1 and not maze[row][col + 1]:
            graph[(row, col)].append(("MoverDerecha-> ", (row, col + 1)))
            graph[(row, col + 1)].append(("MoverIzquierda-> ", (row, col)))
    return graph


def calcular_posicion_ruta(lst_path, start):
    '''Función que devuelve la ruta que encuentra el algoritmo A* dependiendo
    de la posición inicial y destino de los elementos que interactúan.'''
    row = start[0]
    col = start[1]
    ruta = []
    for i in lst_path:
        if i == 'MoverAbajo->':
            row += 1
            ruta.append([i + " ", (row, col)])
        if i == 'MoverArriba->':
            row -= 1
            ruta.append([i + " ", (row, col)])
        if i == 'MoverDerecha->':
            col += 1
            ruta.append([i + " ", (row, col)])
        if i == 'MoverIzquierda->':
            col -= 1
            ruta.append([i + " ", (row, col)])
    return ruta


def heuristic(cell, goal):
    '''Función h'(n) que devuelve la distancia entre dos puntos.'''
    return abs(cell[0] - goal[0]) + abs(cell[1] - goal[1])


def find_path_astar(maze, start, goal, print_=False):
    '''Función que ejecuta el algoritmo A*'''
    if print_:
        print("Start: ", start, " Goal: ", goal)

    # Se crean los elmentos que serivirán para almacenar los nodos que se
    # pueden recorrer según la posición y sus costos.
    pr_queue = []
    lst_cost = []

    # Se agrega a la lista el nodo inicio que tiene costo cero.
    heappush(pr_queue, (0 + heuristic(start, goal), 0, "", start))

    # Se crea la tupla que recibirá las posiciones ya visitadas junto con las
    # direcciones.
    visited = set()

    graph = maze2graph(maze)

    # Ciclo que se ejecuta hasta encontrar la ruta mas optima.
    while pr_queue:
        _, cost, path, current = heappop(pr_queue)
        lst_cost.append(cost)

        # Se verifica si la posición actual es la posición objetivo. Si lo es,
        # devuelve la ruta y termina el ciclo.
        if current == goal:
            return graph, path.split(), max(lst_cost)
        # Se verifica si la posición actual ya ha sido visitada. Si lo ha sido
        # continúa.
        if current in visited:
            continue

        # Lista cerrada donde se gurdan las posiciones ya visitadas.
        visited.add(current)

        # Iteración que permite recorrer la ruta de menor costo hasta el
        # objetivo dependiendo del nodo en el que se encuentra.
        for direction, neighbour in graph[current]:
            # Se agregan a la lista la función de evaluación f(n), el costo de
            # llegar al nodo, la ruta recorrida y los nodos que ya se han
            # procesado y expandido.
            # Donde 'costo + heuristica(vecinos, objetivo)' = g(n) + h'(n) = f(n)
            heappush(pr_queue, (cost + heuristic(neighbour, goal),
                                cost + 1, path + direction, neighbour))
    return "SIN SOLUCION"


def main():
    '''Mapa original, sin elementos.'''
    maze = [[1, 1, 1, 1, 1, 1],
            [1, 0, 1, 0, 0, 1],
            [1, 0, 1, 0, 0, 1],
            [1, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1]]

    # Posiciones iniciales y finales de los elementos que interactúan. No se
    # coloca posición final de R porque es la misma que la posicion final de M1
    pos_Robot = (3, 3)
    targ_M1 = [(1, 1), (4, 4)]
    targ_M2 = [(3, 1), (4, 3)]
    targ_M3 = [(1, 4), (4, 2)]

    # Identificamos la ruta más cercana a los 3 paquetes.
    targets = {'targ_M1': targ_M1, 'targ_M2': targ_M2, 'targ_M3': targ_M3}
    costs = {}
    for i in targets.items():
        graph, path, cost = find_path_astar(maze, pos_Robot, i[1][0], False)
        costs[i[0]] = len(calcular_posicion_ruta(path, pos_Robot))

    # Ordernar por menor costo
    costs = dict(sorted(costs.items(), key=lambda x: x[1]))
    route = {}

    # Ordenamos las rutas en base a los costos.
    for a in costs.items():
        route[a[0]] = targets[a[0]]
    print("COSTOS POR RUTA: ", costs, "\n")
    print("RUTA INCIAL: ", route)
    first = list(route.keys())[0]
    pos_upd = []

    # Ejecutamos los movimientos del robot (R) y traslado de los elementos Ma
    # su posición final.
    for j in list(route.items()):
        print()
        print("**Movimiento recoger paquete")
        print("**Posicion Robot: ", pos_Robot)
        print("**Posicion Destino: ", j[1][0])
        graph, path, cost = find_path_astar(maze, pos_Robot, j[1][0], False)
        print("Camino: ", calcular_posicion_ruta(path, pos_Robot))
        if j[0] != first:
            for k in pos_upd[:]:
                print("Posición nuevo obstaculo: ", k)
                # Se actualiza posición ocupada por el paquete: Nuevo obstaculo
                maze[k[0]][k[1]] = 1
                pos_upd.clear()
        print()
        print("**Movimiento dejar paquete", j)
        pos_Robot = j[1][0]
        print("**Robot antes de movimiento: ", pos_Robot)
        graph, path, cost = find_path_astar(maze, pos_Robot, j[1][1], True)
        print("Camino: ", calcular_posicion_ruta(path, pos_Robot))
        pos_Robot = j[1][1]
        print("**Robot despues de movimiento: ", pos_Robot)
        del route[j[0]]
        print()
        print("RUTA RESTANTE: ", route)
        pos_upd.append([j[1][1][0], j[1][1][1]])

    return 0


if __name__ == '__main__':
    main()
