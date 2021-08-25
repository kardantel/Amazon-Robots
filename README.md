# Amazon Robots

Este repositorio contiene tres soluciones diferentes para un mismo proyecto en el que la empresa Amazon desea utilizar un robot para ordenar el inventario de su bodega. Amazon cuenta con 3 inventarios/productos (mesa con suministros para vender) localizados en unas posiciones específicas de la bodega, representada en una matriz de 4x4. El robot se encarga de dirigirse hacia la posición inicial de cada uno de los 3 inventarios y desplazarlos a una posición final específica.

Un ejemplo del robot, moviendo el inventario, se puede observar en el este [video](https://www.youtube.com/watch?v=UtBa9yVZBJM "CNET News - Meet the robots making Amazon even faster").

### General Features

- Como se mencionó, la bodega (o mapa) tiene un tamaño de 4x4. En la siguiente imagen se pueden observar las posiciones inciales del robot y los 3 inventarios:
![](https://i.imgur.com/AJTbynl.jpg)
- En el mapa arriba:
	- `R` representa el robot. Inicialmente está ubicado en la posición `[2, 2]`;
	- `#` representa una pared;
	- `M1`, `M2`, y `M3` representan los tres inventarios que el robot debe mover. Se encuentran ubicadas en las posiciones `[0 ,0]`, `[2, 0]` y `[0, 3]` respectivamente.
- El robot debe mover los 3 inventarios, M1, M2 y M3, a tres posiciones específicas. Estas posiciones finales se pueden observar en la siguiente imagen:
![](https://i.imgur.com/igt2IlF.jpg)
- El repositorio cuenta con tres soluciones diferentes llamadas `Algorithm1.py`, `Algorithm2.py` y `Algorithm3.py`;
- En los archivos `Algorithm1.py` y `Algorithm2.py` el mapa se representa por medio de una lista donde, `1` son los muros y `0` son los espacios vacíos de la bodega por donde el robot se mueve libremente:
```python
	[[1, 1, 1, 1, 1, 1],
	 [1, 0, 1, 0, 0, 1],
	 [1, 0, 1, 0, 0, 1],
	 [1, 0, 0, 0, 0, 1],
	 [1, 0, 0, 0, 0, 1],
	 [1, 1, 1, 1, 1, 1]]
```
- En el archivo `Algorithm2.py` el mapa se representa por medio de 6 archivos de texto donde, `#` son los muros y `.` son los espacios vacíos de la bodega por donde el robot se mueve libremente (Ver archivos de texto `txt`):
- Cada uno de los códigos arriba descritos implementa la **búsqueda heurística A* ** en Python 3;
- Como función heurística, se utiliza la **Distancia Manhattan**;
- El costo real `g(n)` de cada acción del robot es 1.
- Cada código indica en pantalla, de manera diferente, la secuencia de acciones que realiza el robot para alcanzar el estado objetivo utilizando una notación sencilla.

## Argorithm1.py
- En este código se crearon diccionarios donde se indican las posiciones iniciales y finales tanto del robot, como de los inventarios.
- No se coloca posición final de `R` porque es la misma que la posición final de `M1`.
- La búsqueda heurística A* se encuentra en la función `Astar()`.
- Las coordenadas de orientación del mapa son `N`: Norte, `S`: Sur, `E`: Este, `O`: Oeste.
- Si te gustan los códigos cortos y las salidas sencillas, este archivo es el ideal.

### Out
- Este algoritmo regresa las rutas que recorre el robot: hacia qué inventario o posición de dirige y las coordenadas orientación que toma:
```python
Ruta encontrada:
	Mover R a M3 - Ruta: ENN
	Mover M3 a posF_M3 - Ruta: OSSOS
	Mover R a M2 - Ruta: NO
	Mover M2 a posF_M2 - Ruta: EES
	Mover R a M1 - Ruta: NOONN
	Mover M1 a posF_M1 - Ruta: SSEEES
```

## Argorithm2.py
- Aquí se cambia la nomenclatura del inventario por cuestiones prácticas. Por eso, `A` representa a `M1`, `B` representa a `M2` y `C` representa a `M3`.
- Los mapas de las posiciones iniciales y finales del robot y de cada uno de los inventarios se deben colocar en un documento de texto `txt` para que sea el algoritmo el que encuentre el camino ideal.
- Para este proyecto, se crearon 6 archivos `txt` de acuerdo a la posición del robot y del inventario. Por ejemplo, el archivo con nombre `1mapaR-C` quiere decir que el robot `R` se dirige a la posición del inventario `C`; el archivo con nombre `1mapaC-F` quiere decir que el inventario `C` se dirige a la posición final `F`. Así los demás archivos.
- Los archivos `txt` que contienen los mapas se agregan como cadena de caracteres en una lista y se pasan a la clase `Mapa` que lee los caracteres, las posiciones y los convierte en formato legible para el código.
- La búsqueda heurística A* se encuentra en la clase `AEstrella`.
- Si te gustan los códigos largos, complejos y con salidas gráficas, este archivo es el ideal.

### Out
- Este algoritmo imprime los mapas de cada una de las rutas escogidas por la búsqueda heurística basándose en los mapas originales.
- La ruta encontrada es marcada por los puntos en el mapa. Los demás puntos son eliminados. Por ejemplo, para la ruta del robot `R` que se dirige al inventario `C` (tabla abajo izquierda) y que luego es llevado al punto final (tabla abajo derecha).

| #  | #  |  # | #  | #  | #  |   | #  | #  | #  | #  | #  | #  |
| :------------: | :------------: | :------------: | :------------: | :------------: | :------------: | :------------: | :------------: | :------------: | :------------: | :------------: | :------------: | :------------: |
| #  |   | #  | ·  | C  | #  |   | #  |   | #  |   | R  | #  |
| #  |   | #  | ·  |   | #  |   | #  |   | #  |   | ·  | #  |
| #  |   |   | R  |   | #  |   | #  |   |   |   | ·  | #  |
| #  |   |   |   |   | #  |   | #  |   | F  | ·  | ·  | #  |
| #  | #  | #  | #  | #  | #  |   | #  | #  | #  | #  | #  | #  |

## Argorithm3.py
- El algoritmo detecta qué inventario está más cerca de la primera posición del robot `R` y encuentra la ruta más óptima.
- La búsqueda heurística A* se encuentra en la función `find_path_astar()`.
- Al igual que en `Argorithm1.py`, el mapa se representa por medio de una lista.
- Sin embargo, a diferencia de `Argorithm1.py`, se crearon listas (en vez de diccionarios) donde se indican las posiciones iniciales y finales tanto del robot, como de los inventarios.
- Si te gustan los códigos no tan largos y las salidas detalladas, este archivo es el ideal.
- Tampoco se coloca posición final de `R` porque es la misma que la posición final de `M1`. En la imagen abajo se pueden observar las direcciones y posiciones del robot y de los inventarios:
![](https://i.imgur.com/jpkhjSd.png)

### Out
- Este algoritmo imprime con bastante detalle: qué tipo de movimiento está haciendo el robot `R` y, la posición inicial del recorrido y la posición final: recoger inventario o dejar inventario en destino.
- Así mismo, detalla el camino recorrido dependiendo de la dirección y la posición del mapa a la que se dirige. Por ejemplo, si nos ubicamos en la posición `(3, 3)` (que es la posición inicial de `R`), se nos indicará que nos desplazamos hacia `Arriba` a la posición `(2, 3)`, a la `Derecha` a la posición `(3, 4)`, `Abajo` a la posición `(4, 3)` y a la `Izquierda` a la posición `(3, 2)`, de la siguiente forma:
```python
 {..., (3, 3): [('MoverIzquierda-> ', (3, 2)), ('MoverArriba-> ', (2, 3)), ('MoverAbajo-> ', (4, 3)), ('MoverDerecha-> ', (3, 4)), ...}
```
