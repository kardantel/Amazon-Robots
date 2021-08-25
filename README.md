# Amazon Robots

Este repositorio contiene tres soluciones diferentes para un mismo proyecto en el que la empresa Amazon desea utilizar un robot para ordenar el inventario de su bodega. Amazon cuenta con 3 inventarios/productos (mesa con suministros para vender) localizados en unas posiciones específicas de la bodega, representada en una matriz de 4x4. El robot se encarga de dirigirse hacia la posición inicial de cada uno de los 3 inventarios y desplazarlos a una posición final específica.

Un ejemplo del robot, moviendo el inventario, se puede observar en el este [video](https://www.youtube.com/watch?v=UtBa9yVZBJM "CNET News - Meet the robots making Amazon even faster").

### Features

- Como se mencionó, la bodega (o mapa) tiene un tamaño de 4x4. En la siguiente imagen se pueden observar las posiciones inciales del robot y los 3 inventarios:
![](https://i.imgur.com/AJTbynl.jpg)
- En el mapa arriba:
	- `R` representa el robot. Inicialmente está ubicado en la posición `[2, 2]`;
	- `#` representa una pared;
	- `M1`, `M2`, y `M3` representan los tres inventarios que el robot debe mover. Se encuentran ubicadas en las posiciones `[0 ,0]`, `[2, 0]` y `[0, 3]` respectivamente.
- El robot debe mover los 3 inventarios, M1, M2 y M3, a tres posiciones específicas. Estas posiciones finales se pueden observar en la siguiente imagen:
![](https://i.imgur.com/igt2IlF.jpg)
- El repositorio cuenta con tres soluciones diferentes llamadas `Algorithm1.py`, `Algorithm2.py` y `Algorithm3.py`;
- Cada uno de los códigos arriba descritos implementa la **búsqueda heurística A* ** en Python 3;
- Como función heurística, se utiliza la **Distancia Manhattan**;
- El costo real `g(n)` de cada acción del robot es 1.
- Cada código indica en pantalla, de manera diferente, la secuencia de acciones que realiza el robot para alcanzar el estado objetivo utilizando una notación sencilla.
- A continuación, se describen cada una de la soluciones realizadas para este proyecto.

## Argorithm1.py


## Argorithm2.py


## Argorithm3.py
