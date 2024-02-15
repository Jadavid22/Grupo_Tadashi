## Práctica 1: Aprendiendo a Usar nand2tetris e Implementación de Compuertas Lógicas

### Introducción:
En esta práctica exploraremos la implementación de compuertas lógicas básicas utilizando el software nand2tetris, con el apoyo del entorno de desarrollo Visual Studio Code. El propósito es comprender y diseñar compuertas lógicas fundamentales, como NOT, AND, OR, XOR, entre otras, teniendo únicamente a la puerta lógica NAND como base.

Para comenzar, descargamos el software nand2tetris, que nos proporciona una plataforma interactiva para construir desde cero un computador completo, incluyendo hardware y software, desde los niveles más básicos hasta los más complejos. Así pues, usaremos [este vídeo](https://www.youtube.com/watch?v=xUFpmKa7f7Y&list=PLrDd_kMiAuNmSb-CKWQqq9oBFN_KNMTaI&index=5) como referencia para la instalación.

Con la ayuda de [Visual Studio Code](https://code.visualstudio.com/), un entorno de desarrollo integrado (IDE) altamente versátil, editaremos y escribiremos el código necesario para implementar las compuertas lógicas. Visual Studio ofrece herramientas poderosas para la escritura de código, depuración y gestión de proyectos, lo que facilita enormemente el proceso de desarrollo.

Una vez que tenemos el entorno preparado, comenzamos a diseñar nuestras compuertas lógicas. La elección de la puerta NAND como base se debe a su capacidad para implementar cualquier otra compuerta lógica. Dicho esto, hacemos uso del lenguaje de descripción de hardware (HDL) proporcionado por nand2tetris para escribir el código que define el comportamiento de nuestras compuertas.

Después de tener el código en Visual Studio, lo probamos en el entorno de simulación de nand2tetris. Esta fase es crucial para verificar que nuestras compuertas funcionan correctamente según las especificaciones lógicas esperadas. Si hay errores, volvemos al código en Visual Studio para corregirlos y repetimos el proceso de prueba.

### Objetivo:
Construir todas las compuertas lógicas descritas en la Figura 1 para obtener un conjunto de chips básicos. Los únicos bloques de construcción que podemos utilizar en este proyecto son las compuertas Nand primitivas y las compuertas compuestas que iremos construyendo gradualmente sobre ellas.

**Figura 1.** Listado de Compuertas Lógicas que van a Desarrollarse.


![Compuertas Lógicas a Realizar](https://i.ibb.co/g9c1s3n/Captura-de-pantalla-2024-02-11-091133.png)

**Nota.** Imagen obtenida de: https://www.nand2tetris.org/project01

## Solución de Compuertas Lógicas

### NOT:
La compuerta lógica NOT se implementa utilizando exclusivamente la compuerta NAND como base. La compuerta NOT, también conocida como inversor, tiene una única entrada y una única salida, y su función es invertir el valor de la entrada.
La implementación de la compuerta NOT utilizando NAND se logra conectando ambas entradas de la NAND a la misma señal de entrada. El resultado es que cuando la entrada es 0, la salida de la NAND será 1, y viceversa. Esto crea una inversión del valor de entrada, que es exactamente la función de una compuerta NOT.

**Figura 2.** Representación Compuerta NOT


![Explicación NOT](https://i.ibb.co/LnkbDDx/Captura-de-pantalla-2024-02-14-204755.png)

**Figura 3.** Código Compuerta NOT


![Código NOT](https://i.ibb.co/YT9FCP9/Captura-de-pantalla-2024-02-14-204602.png)

### OR:
La primera compuerta NOT niega la entrada A y la segunda compuerta NOT niega la entrada B. Luego, pasamos estas negaciones como entradas a una tercera compuerta NAND, que simula la operación OR. La salida de esta última compuerta NAND será la salida de la compuerta OR.

**Figura 4.** Representación Compuerta OR


![Explicación OR](https://i.ibb.co/5nm8bqx/Captura-de-pantalla-2024-02-14-205059.png)

**Figura 5.** Código Compuerta OR


![Código OR](https://i.ibb.co/WfnZfZp/Captura-de-pantalla-2024-02-14-204933.png)

### AND:
La construcción de una compuerta AND se basa en la utilización de una compuerta NAND y una compuerta NOT. Básicamente, como AND es el inverso de NAND, solo debemos negar el resultado de NAND.

**Figura 6.** Representación Compuerta AND


![Explicación AND](https://i.ibb.co/chnm7cH/Captura-de-pantalla-2024-02-14-205600.png)

**Figura 7.** Código Compuerta AND


![Código AND](https://i.ibb.co/vVVR3CF/Captura-de-pantalla-2024-02-14-205507.png)

### XOR:
Para implementar una compuerta XOR (o exclusiva) utilizaremos compuertas NOT, AND y OR. Podemos seguir el enfoque del diseño lógico digital, ya que la compuerta XOR devuelve un resultado verdadero (1) cuando hay un número impar de entradas verdaderas.

**Figura 8.** Representación Compuerta XOR


![Explicación XOR](https://i.ibb.co/G2BGrjH/Captura-de-pantalla-2024-02-14-210507.png)

**Figura 9.** Código Compuerta XOR


![Código XOR](https://i.ibb.co/fdGDhmN/Captura-de-pantalla-2024-02-14-210426.png)


### Mux:
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus convallis vulputate facilisis. Ut auctor eu enim vitae pharetra. Cras ultrices consequat diam, sed ultrices ex condimentum non. Curabitur vehicula nunc id ipsum gravida accumsan. Praesent interdum id ante et congue. Cras ut risus ultrices, luctus elit sit amet, mollis quam. Nulla eleifend lobortis ullamcorper. Ut eleifend cursus maximus. Morbi vitae ante vitae odio lobortis mattis. Praesent vestibulum est et tellus sollicitudin iaculis. Sed imperdiet odio ac dui hendrerit maximus. Donec at bibendum dolor.

### DMux:
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus convallis vulputate facilisis. Ut auctor eu enim vitae pharetra. Cras ultrices consequat diam, sed ultrices ex condimentum non. Curabitur vehicula nunc id ipsum gravida accumsan. Praesent interdum id ante et congue. Cras ut risus ultrices, luctus elit sit amet, mollis quam. Nulla eleifend lobortis ullamcorper. Ut eleifend cursus maximus. Morbi vitae ante vitae odio lobortis mattis. Praesent vestibulum est et tellus sollicitudin iaculis. Sed imperdiet odio ac dui hendrerit maximus. Donec at bibendum dolor.

### Not16
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus convallis vulputate facilisis. Ut auctor eu enim vitae pharetra. Cras ultrices consequat diam, sed ultrices ex condimentum non. Curabitur vehicula nunc id ipsum gravida accumsan. Praesent interdum id ante et congue. Cras ut risus ultrices, luctus elit sit amet, mollis quam. Nulla eleifend lobortis ullamcorper. Ut eleifend cursus maximus. Morbi vitae ante vitae odio lobortis mattis. Praesent vestibulum est et tellus sollicitudin iaculis. Sed imperdiet odio ac dui hendrerit maximus. Donec at bibendum dolor.

### And16
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus convallis vulputate facilisis. Ut auctor eu enim vitae pharetra. Cras ultrices consequat diam, sed ultrices ex condimentum non. Curabitur vehicula nunc id ipsum gravida accumsan. Praesent interdum id ante et congue. Cras ut risus ultrices, luctus elit sit amet, mollis quam. Nulla eleifend lobortis ullamcorper. Ut eleifend cursus maximus. Morbi vitae ante vitae odio lobortis mattis. Praesent vestibulum est et tellus sollicitudin iaculis. Sed imperdiet odio ac dui hendrerit maximus. Donec at bibendum dolor.

### Or16
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
Esta compuerta necesita un total de 4 entradas de 16 bits, por lo que podríamos usar el chip Mux16. De igual forma, la lógica será muy similar a la compuerta DMux4Way.

#### Resolución:
- Vamos a usar tres compuertas Max16, para comodidad les daremos los alias [1], [2] y [3] para una mejor comprensión.
- Dos compuertas van a tomar los inputs para luego enviarlos a un solo output, así que [3] se va a conectar con el output.
- [3] tendrá que escoger a cuál de las otras dos compuertas está escuchando, por lo que le daremos importancia al bit más significativo (bit 1) y le pasamos ese valor al selector.
- Para los inputs de [1] y [2] trabajaremos desde afuera hacia dentro, así que el orden sería a=a, b=b, a=c, b=d respectivamente.
- Ahora, el selector en [1] y [2] será el bit menos significativo (bit 0).
- Asignamos algún nombre a los dos outputs de las entradas y le pasamos esos valores como inputs a [3].

#### Código:
![Código Mux4Way16](https://i.ibb.co/ZNhtWNC/Mux4-Way16-1.png)

### Mux8Way16
En este punto ya hemos implementado un Demultiplexor de 8 vías, por lo que podríamos seguir el mismo procedimiento solo que este iría "invertido".

#### Resolución:
- Utilizaremos dos compuertas Mux4Way16 y un Mux16.
- El output lo conectamos con el Mux16 y ahora el bit más significativo lo dejamos en 2.
- Las dos compuertas Mux4Way16 usarán los bits menos significativos (0 y 1).
- Nombramos las dos salidas de las compuertas Mux4Way16 y pasamos esos valores como inputs del Mux16.
- Las entradas de las dos compuertas Mux4Way16 van a ser desde afuera hacia dentro, por lo que el orden sería: a=a, b=b, c=c, d=d, a=e, b=f, c=g, d=h respectivamente.

#### Código:
![Código Mux8Way16](https://i.ibb.co/nBTHJ5s/Mux8-Way16-1.png)

## Referencias
[1] https://www.youtube.com/watch?v=Mzy0RG9Z1Ak (From NAND To Tetris - Logic Gates Lab).


[2] https://www.nand2tetris.org/project01 (From Nand to Tetris Sitio Web).


[3] Trabajos y Prácticas Rueltas de Semestres Anteriores.
