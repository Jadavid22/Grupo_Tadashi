## Práctica 1: Introducción a nand2tetris e Implementación de Compuertas Lógicas
### Resumen: 
Una arquitectura de computadora típica se basa en un conjunto de compuertas lógicas elementales como And, Or, Mux, etc., así como sus versiones bit a bit And16, Or16, Mux16, etc. (asumiendo una máquina de 16 bits). Este proyecto nos involucra en la construcción de un conjunto típico de compuertas lógicas básicas que forman los bloques de construcción elementales a partir de los cuales más tarde construiremos la CPU y la RAM de la computadora.
### Objetivo:
Construir todas las puertas lógicas descritas en la Figura 1, produciendo un conjunto de chips básico. Los únicos bloques de construcción que podemos utilizar en este proyecto son las puertas Nand primitivas y las puertas compuestas que construirá gradualmente sobre ellas.

## Compuertas Requeridas
![Compuertas Lógicas a Realizar](https://i.ibb.co/g9c1s3n/Captura-de-pantalla-2024-02-11-091133.png)

### NOT:
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus convallis vulputate facilisis. Ut auctor eu enim vitae pharetra. Cras ultrices consequat diam, sed ultrices ex condimentum non. Curabitur vehicula nunc id ipsum gravida accumsan. Praesent interdum id ante et congue. Cras ut risus ultrices, luctus elit sit amet, mollis quam. Nulla eleifend lobortis ullamcorper. Ut eleifend cursus maximus. Morbi vitae ante vitae odio lobortis mattis. Praesent vestibulum est et tellus sollicitudin iaculis. Sed imperdiet odio ac dui hendrerit maximus. Donec at bibendum dolor.

### OR:
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus convallis vulputate facilisis. Ut auctor eu enim vitae pharetra. Cras ultrices consequat diam, sed ultrices ex condimentum non. Curabitur vehicula nunc id ipsum gravida accumsan. Praesent interdum id ante et congue. Cras ut risus ultrices, luctus elit sit amet, mollis quam. Nulla eleifend lobortis ullamcorper. Ut eleifend cursus maximus. Morbi vitae ante vitae odio lobortis mattis. Praesent vestibulum est et tellus sollicitudin iaculis. Sed imperdiet odio ac dui hendrerit maximus. Donec at bibendum dolor.

### AND:
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus convallis vulputate facilisis. Ut auctor eu enim vitae pharetra. Cras ultrices consequat diam, sed ultrices ex condimentum non. Curabitur vehicula nunc id ipsum gravida accumsan. Praesent interdum id ante et congue. Cras ut risus ultrices, luctus elit sit amet, mollis quam. Nulla eleifend lobortis ullamcorper. Ut eleifend cursus maximus. Morbi vitae ante vitae odio lobortis mattis. Praesent vestibulum est et tellus sollicitudin iaculis. Sed imperdiet odio ac dui hendrerit maximus. Donec at bibendum dolor.

### XOR:
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus convallis vulputate facilisis. Ut auctor eu enim vitae pharetra. Cras ultrices consequat diam, sed ultrices ex condimentum non. Curabitur vehicula nunc id ipsum gravida accumsan. Praesent interdum id ante et congue. Cras ut risus ultrices, luctus elit sit amet, mollis quam. Nulla eleifend lobortis ullamcorper. Ut eleifend cursus maximus. Morbi vitae ante vitae odio lobortis mattis. Praesent vestibulum est et tellus sollicitudin iaculis. Sed imperdiet odio ac dui hendrerit maximus. Donec at bibendum dolor.

### Mux:
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus convallis vulputate facilisis. Ut auctor eu enim vitae pharetra. Cras ultrices consequat diam, sed ultrices ex condimentum non. Curabitur vehicula nunc id ipsum gravida accumsan. Praesent interdum id ante et congue. Cras ut risus ultrices, luctus elit sit amet, mollis quam. Nulla eleifend lobortis ullamcorper. Ut eleifend cursus maximus. Morbi vitae ante vitae odio lobortis mattis. Praesent vestibulum est et tellus sollicitudin iaculis. Sed imperdiet odio ac dui hendrerit maximus. Donec at bibendum dolor.

### DMux:
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus convallis vulputate facilisis. Ut auctor eu enim vitae pharetra. Cras ultrices consequat diam, sed ultrices ex condimentum non. Curabitur vehicula nunc id ipsum gravida accumsan. Praesent interdum id ante et congue. Cras ut risus ultrices, luctus elit sit amet, mollis quam. Nulla eleifend lobortis ullamcorper. Ut eleifend cursus maximus. Morbi vitae ante vitae odio lobortis mattis. Praesent vestibulum est et tellus sollicitudin iaculis. Sed imperdiet odio ac dui hendrerit maximus. Donec at bibendum dolor.

### Not16
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus convallis vulputate facilisis. Ut auctor eu enim vitae pharetra. Cras ultrices consequat diam, sed ultrices ex condimentum non. Curabitur vehicula nunc id ipsum gravida accumsan. Praesent interdum id ante et congue. Cras ut risus ultrices, luctus elit sit amet, mollis quam. Nulla eleifend lobortis ullamcorper. Ut eleifend cursus maximus. Morbi vitae ante vitae odio lobortis mattis. Praesent vestibulum est et tellus sollicitudin iaculis. Sed imperdiet odio ac dui hendrerit maximus. Donec at bibendum dolor.

### And16
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus convallis vulputate facilisis. Ut auctor eu enim vitae pharetra. Cras ultrices consequat diam, sed ultrices ex condimentum non. Curabitur vehicula nunc id ipsum gravida accumsan. Praesent interdum id ante et congue. Cras ut risus ultrices, luctus elit sit amet, mollis quam. Nulla eleifend lobortis ullamcorper. Ut eleifend cursus maximus. Morbi vitae ante vitae odio lobortis mattis. Praesent vestibulum est et tellus sollicitudin iaculis. Sed imperdiet odio ac dui hendrerit maximus. Donec at bibendum dolor.

### Mux16
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus convallis vulputate facilisis. Ut auctor eu enim vitae pharetra. Cras ultrices consequat diam, sed ultrices ex condimentum non. Curabitur vehicula nunc id ipsum gravida accumsan. Praesent interdum id ante et congue. Cras ut risus ultrices, luctus elit sit amet, mollis quam. Nulla eleifend lobortis ullamcorper. Ut eleifend cursus maximus. Morbi vitae ante vitae odio lobortis mattis. Praesent vestibulum est et tellus sollicitudin iaculis. Sed imperdiet odio ac dui hendrerit maximus. Donec at bibendum dolor.

### Or8Way
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus convallis vulputate facilisis. Ut auctor eu enim vitae pharetra. Cras ultrices consequat diam, sed ultrices ex condimentum non. Curabitur vehicula nunc id ipsum gravida accumsan. Praesent interdum id ante et congue. Cras ut risus ultrices, luctus elit sit amet, mollis quam. Nulla eleifend lobortis ullamcorper. Ut eleifend cursus maximus. Morbi vitae ante vitae odio lobortis mattis. Praesent vestibulum est et tellus sollicitudin iaculis. Sed imperdiet odio ac dui hendrerit maximus. Donec at bibendum dolor.

### DMux4Way
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus convallis vulputate facilisis. Ut auctor eu enim vitae pharetra. Cras ultrices consequat diam, sed ultrices ex condimentum non. Curabitur vehicula nunc id ipsum gravida accumsan. Praesent interdum id ante et congue. Cras ut risus ultrices, luctus elit sit amet, mollis quam. Nulla eleifend lobortis ullamcorper. Ut eleifend cursus maximus. Morbi vitae ante vitae odio lobortis mattis. Praesent vestibulum est et tellus sollicitudin iaculis. Sed imperdiet odio ac dui hendrerit maximus. Donec at bibendum dolor.

### DMux8Way
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus convallis vulputate facilisis. Ut auctor eu enim vitae pharetra. Cras ultrices consequat diam, sed ultrices ex condimentum non. Curabitur vehicula nunc id ipsum gravida accumsan. Praesent interdum id ante et congue. Cras ut risus ultrices, luctus elit sit amet, mollis quam. Nulla eleifend lobortis ullamcorper. Ut eleifend cursus maximus. Morbi vitae ante vitae odio lobortis mattis. Praesent vestibulum est et tellus sollicitudin iaculis. Sed imperdiet odio ac dui hendrerit maximus. Donec at bibendum dolor.

### Mux4Way16
Esta compuerta necesita un total de 4 entradas de 16 bits, por lo que podríamos usar el chip Mux16. De igual forma, la lógica será muy similar a la compuerta 4-Way Demux.

#### Resolución:
- Vamos a usar tres compuertas Max16, para comodidad les daremos los alias [1], [2] y [3] para una mejor comprensión.
- Dos compuertas van a tomar los inputs para luego enviarlos a un solo output, así que [3] se va a conectar con el output.
- [3] tendrá que escoger a cuál de las otras dos compuertas está escuchando, por lo que le daremos importancia al bit más significativo (bit 1) y le pasamos ese valor al selector.
- Para los inputs de [1] y [2] trabajaremos desde afuera hacia dentro, así que el orden sería a=a, b=b, a=c, b=d respectivamente.
- Ahora, el selector en [1] y [2] será el bit menos significativo (bit 0).
- Asignamos algún nombre a los dos outputs de las entradas y le pasamos esos valores como inputs a [3].

#### Resultados:
![Código Mux4Way16](https://i.ibb.co/VvMbDXL/Captura-de-pantalla-2024-02-11-192338.png)


### Mux8Way16
En este punto ya hemos implementado un Demultiplexor de 8 vías, por lo que podríamos seguir el mismo procedimiento solo que este iría "invertido".

#### Resolución:
- Utilizaremos dos compuertas Mux4Way16 y un Mux16.
- El output lo conectamos con el Mux16 y ahora el bit más significativo lo dejamos en 2.
- Las dos compuertas Mux4Way16 usarán los bits menos significativos (0 y 1).
- Nombramos las dos salidas de las compuertas Mux4Way16 y pasamos esos valores como inputs del Mux16.
- Las entradas de las dos compuertas Mux4Way16 van a ser desde afuera hacia dentro, por lo que el orden sería: a=a, b=b, c=c, d=d, a=e, b=f, c=g, d=h respectivamente.

#### Resultados:
![Código Mux8Way16](https://i.ibb.co/FKWsM18/Captura-de-pantalla-2024-02-11-213024.png)

## Referencias
[1] https://www.youtube.com/watch?v=Mzy0RG9Z1Ak (From NAND To Tetris - Logic Gates Lab).


[2] https://www.nand2tetris.org/project01 (From Nand to Tetris Sitio Web).


[3] Trabajos y Prácticas Rueltas de Semestres Anteriores.
