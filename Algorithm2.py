# Clases
# ---------------------------------------------------------------------


class Mapa:
    def __init__(self, archivo):
        self.mapa = leerMapa(archivo)
        self.fil = len(self.mapa)
        self.col = len(self.mapa[0])

    def __str__(self):
        salida = ""
        for f in range(self.fil):
            for c in range(self.col):
                if self.mapa[f][c] == 0:
                    salida += "  "
                if self.mapa[f][c] == 1:
                    salida += "# "
                if self.mapa[f][c] == 2:
                    salida += "R "
                if self.mapa[f][c] == 3:
                    salida += "A "
                if self.mapa[f][c] == 4:
                    salida += "B "
                if self.mapa[f][c] == 5:
                    salida += "C "
                if self.mapa[f][c] == 6:
                    salida += "F "
                if self.mapa[f][c] == 7:
                    salida += ". "
            salida += "\n"
        return salida

    def camino(self, lista):
        del lista[-1]
        for i in range(len(lista)):
            self.mapa[lista[i][0]][lista[i][1]] = 7


class Nodo:
    def __init__(self, pos=[0, 0], padre=None):
        self.pos = pos
        self.padre = padre
        self.h = distancia(self.pos, pos_f)

        if self.padre is None:
            self.g = 0
        else:
            self.g = self.padre.g + 1
        self.f = self.g + self.h    # Función de evaluación f(n).


class AEstrella:
    def __init__(self, mapa, j):
        self.mapa = mapa

        # Nodos de inicio y fin.
        self.inicio = Nodo(buscarPos(2, mapa))
        self.fin = Nodo(buscarPos(j, mapa))

        # Crea las listas abierta y cerrada.
        self.abierta = []
        self.cerrada = []

        # Añade el nodo inicial a la lista cerrada.
        self.cerrada.append(self.inicio)

        # Añade vecinos a la lista abierta
        self.abierta += self.vecinos(self.inicio)

        # Buscar mientras objetivo no este en la lista cerrada.
        while self.objetivo():
            self.buscar()

        self.camino = self.caminoAE()

    def vecinos(self, nodo):
        '''Devuelve una lista con los nodos vecinos transitables.'''
        vecinos = []
        if self.mapa.mapa[nodo.pos[0] + 1][nodo.pos[1]] != 1:
            vecinos.append(Nodo([nodo.pos[0] + 1, nodo.pos[1]], nodo))
            # print("de")
        if self.mapa.mapa[nodo.pos[0] - 1][nodo.pos[1]] != 1:
            vecinos.append(Nodo([nodo.pos[0] - 1, nodo.pos[1]], nodo))
            # print("iz")
        if self.mapa.mapa[nodo.pos[0]][nodo.pos[1] - 1] != 1:
            vecinos.append(Nodo([nodo.pos[0], nodo.pos[1] - 1], nodo))
            # print("ab")
        if self.mapa.mapa[nodo.pos[0]][nodo.pos[1] + 1] != 1:
            vecinos.append(Nodo([nodo.pos[0], nodo.pos[1] + 1], nodo))
            # print("ar")
        return vecinos

    def f_menor(self):
        '''Pasa el elemento de f menor de la lista abierta a la cerrada.'''
        a = self.abierta[0]
        n = 0
        for i in range(1, len(self.abierta)):
            if self.abierta[i].f < a.f:
                a = self.abierta[i]
                n = i
        self.cerrada.append(self.abierta[n])
        del self.abierta[n]

    def en_lista(self, nodo, lista):
        '''Comprueba si un nodo está en una lista.'''
        for i in range(len(lista)):
            if nodo.pos == lista[i].pos:
                return 1
        return 0

    def ruta(self):
        '''Gestiona los vecinos del nodo seleccionado.'''
        for i in range(len(self.nodos)):
            if self.en_lista(self.nodos[i], self.cerrada):
                continue
            elif not self.en_lista(self.nodos[i], self.abierta):
                self.abierta.append(self.nodos[i])
            else:
                if self.select.g + 1 < self.nodos[i].g:
                    for j in range(len(self.abierta)):
                        if self.nodos[i].pos == self.abierta[j].pos:
                            del self.abierta[j]
                            self.abierta.append(self.nodos[i])
                            break

    def buscar(self):
        '''Analiza el último elemento de la lista cerrada.'''
        self.f_menor()
        self.select = self.cerrada[-1]
        self.nodos = self.vecinos(self.select)
        self.ruta()

    def objetivo(self):
        '''Comprueba si el objetivo está en la lista abierta.'''
        for i in range(len(self.abierta)):
            if self.fin.pos == self.abierta[i].pos:
                return 0
        return 1

    def caminoAE(self):
        '''Retorna una lista con las posiciones del camino a seguir.'''
        for i in range(len(self.abierta)):
            if self.fin.pos == self.abierta[i].pos:
                objetivo = self.abierta[i]

        camino = []
        while objetivo.padre is not None:
            camino.append(objetivo.pos)
            objetivo = objetivo.padre
        camino.reverse()
        return camino

# ---------------------------------------------------------------------


# Funciones
# ---------------------------------------------------------------------

def buscarPos(x, mapa):
    '''Devuelve la posición de "x" en una lista.'''
    for f in range(mapa.fil):
        for c in range(mapa.col):
            if mapa.mapa[f][c] == x:
                return [f, c]
    return 0


def distancia(a, b):
    '''Distancia entre dos puntos.'''
    return abs(a[0] - b[0]) + abs(a[1] - b[1])  # Valor absoluto.


def quitarUltimo(lista):
    '''Quita el último caracter de una lista.'''
    for i in range(len(lista)):
        lista[i] = lista[i][:-1]
    return lista


def listarCadena(cadena):
    '''Covierte una cadena en una lista.'''
    lista = []
    for i in range(len(cadena)):
        if cadena[i] == ".":
            lista.append(0)
        if cadena[i] == "#":
            lista.append(1)
        if cadena[i] == "R":
            lista.append(2)
        if cadena[i] == "A":    # A -> M1
            lista.append(3)
        if cadena[i] == "B":    # B -> M2
            lista.append(4)
        if cadena[i] == "C":    # C -> M3
            lista.append(5)
        if cadena[i] == "F":
            lista.append(6)
    return lista


def leerMapa(archivo):
    '''Lee un archivo de texto y lo convierte en una lista.'''
    mapa = open(archivo, "r")
    mapa = mapa.readlines()
    for i in range(len(mapa)):
        mapa[i] = listarCadena(mapa[i])
    return mapa

# ---------------------------------------------------------------------


def main():
    mapasList = ["1mapaR-C.txt", "2mapaC-F.txt", "3mapaR-B.txt",
                 "4mapaB-F.txt", "5mapaR-A.txt", "6mapaA-F.txt"]
    Mx = [5, 6, 4, 6, 3, 6]
    for map, fin in zip(mapasList, Mx):
        mapa = Mapa(map)
        globals()["pos_f"] = buscarPos(fin, mapa)
        A = AEstrella(mapa, fin)
        # print(A.abierta)
        mapa.camino(A.camino)
        print(mapa)
    return 0


if __name__ == '__main__':
    main()
