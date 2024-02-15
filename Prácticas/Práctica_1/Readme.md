## Práctica 1: Aprendiendo a Usar nand2tetris e Implementación de Chips Lógicos

### Introducción:
En esta práctica exploraremos la implementación de chips lógicos básicos utilizando el software nand2tetris, con el apoyo del entorno de desarrollo Visual Studio Code. El propósito es comprender y diseñar estos componentes lógicos fundamentales, como NOT, AND, OR, XOR, entre otros, teniendo únicamente a la puerta lógica NAND como base.

Para comenzar, descargamos el software nand2tetris, que nos proporciona una plataforma interactiva para construir desde cero un computador completo, incluyendo hardware y software, desde los niveles más básicos hasta los más complejos. Así pues, usaremos [este vídeo](https://www.youtube.com/watch?v=xUFpmKa7f7Y&list=PLrDd_kMiAuNmSb-CKWQqq9oBFN_KNMTaI&index=5) como referencia para la instalación.

Con la ayuda de [Visual Studio Code](https://code.visualstudio.com/), un entorno de desarrollo integrado (IDE) altamente versátil, editaremos y escribiremos el código necesario para implementar las compuertas lógicas. Visual Studio ofrece herramientas poderosas para la escritura de código, depuración y gestión de proyectos, lo que facilita enormemente el proceso de desarrollo.

Una vez que tenemos el entorno preparado, comenzamos a diseñar nuestros chips lógicos. La elección de la puerta NAND como base se debe a su capacidad para implementar cualquier otro chip lógico a partir de ella. Dicho esto, hacemos uso del lenguaje de descripción de hardware (HDL) proporcionado por nand2tetris para escribir el código que define el comportamiento de nuestros chips.

Después de tener el código en Visual Studio, lo probamos en el entorno de simulación de nand2tetris. Esta fase es crucial para verificar que nuestras implementaciones funcionan correctamente según las especificaciones lógicas esperadas. Si hay errores, volvemos al código en Visual Studio para corregirlos y repetimos el proceso de prueba.

### Objetivo:
Construir todos los componentes lógicos descritos en la Figura 1 para obtener un conjunto de chips básicos. Los únicos bloques de construcción que podemos utilizar en este proyecto son las compuertas Nand primitivas y los chips compuestos que iremos construyendo gradualmente.

**Figura 1.** Listado de Chips Lógicos que van a Desarrollarse.


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
Para implementar una compuerta XOR (o exclusiva) utilizaremos compuertas NOT, AND y OR. Primero necesitamos negar las entradas a y b con compuertas NOT, luego pasamos a una AND el resultado de cada NOT con la variable opuesta sin negar. Por ejemplo, a sin negar y b negada. Finalmente, los resultados de esas compuertas AND los pasamos una compuerta OR y ya obtendríamos los resultados que estamos buscando.

**Figura 8.** Representación Compuerta XOR


![Explicación XOR](https://i.ibb.co/G2BGrjH/Captura-de-pantalla-2024-02-14-210507.png)

**Figura 9.** Código Compuerta XOR


![Código XOR](https://i.ibb.co/fdGDhmN/Captura-de-pantalla-2024-02-14-210426.png)


### Mux:
En este chip tenemos una nueva variable de entrada: el selector. Como este afecta directamente a la salida dependiendo del estado que tenga, lo vamos a negar primero con una NOT. Ahora bien, necesitamos que si el selector está en 0, la salida sea a, por lo que usaremos una AND que de parámetros reciba al selector negado y a a. Asimismo, si el selector está en 1, la salida será b, entonces en otra AND le pasamos de parámetros al selector sin negar y a b. Finalmente, los resultados de ambas AND las mandamos como parámetros a una OR y ya obtenemos al multiplexor.

**Figura 10.** Código Chip MUX


![Código Mux](https://i.ibb.co/T0cyLD8/Captura-de-pantalla-2024-02-14-233529.png)


### DMux:
Primer chip en incluir dos salidas (a y b) y dos entradas (in y sel). Usaremos una NOT para el selector, ya que si el valor de este es 1, la salida será b; si el selector es 0, la salida será a, por lo que vamos a usar dos AND de la siguiente manera:

- La primera recibe a in y al selector sin negar.
- La segunda recibe al selector negado y a in.

**Figura 11.** Código Chip DMux


![Código DMux](https://i.ibb.co/phcDsMS/Captura-de-pantalla-2024-02-15-000003.png)

### Not16
Bastante sencilla de entender e implementar: 16 posibles entradas y todas las que pasen, saldrán negadas. Simplemente vamos a usar 16 compuertas NOT (una para cada entrada) y listo.

**Figura 12.** Código Chip Not16


![Código Not16](https://i.ibb.co/FH4QxBw/Captura-de-pantalla-2024-02-15-000739.png)

### And16
En términos conceptuales, será muy similar al Not16, pues aquí también vamos a usar 16 compuertas AND y la estructura será casi la misma: como tenemos dos entradas (a y b) y una sola salida, cada AND va a estar destinada a una pareja de inputs específicos (0-0, 1-1, 2-2, y así sucesivamente). 

**Figura 13.** Código Chip And16


![Código Ans16](https://i.ibb.co/cCsCD9j/Captura-de-pantalla-2024-02-15-003657.png)

### Or16
Súper sencilla: cambiar del código de And16 todos los AND por OR. Esto debido a que sigue las mismas reglas para sus resultados, lo único distinto es la operación que se realiza sobre las entradas.

**Figura 14.** Código Chip Or16


![Código Or16](https://i.ibb.co/MZ3N226/Captura-de-pantalla-2024-02-15-004103.png)

### Mux16
Debemos repetir 16 veces la compuerta Mux. Se tendrán dos entradas a y b y dos vectores con 16 valores a y b y el selector "sel". A continuación, se repetirá 16 veces la compuerta Mux para cada una de las entradas de los vectores.

**Figura 15.** Representación Compuerta Mux16


![Explicación Mux16](https://i.ibb.co/BGXhqWs/Captura-de-pantalla-2024-02-15-140507.png)

**Figura 16.** Código Compuerta Mux16


![Código Mux16](https://i.ibb.co/vBwq1LK/Captura-de-pantalla-2024-02-15-140624.png)

### Or8Way
Aquí podemos aplicar un proceso de reducción, ya que todas las ocho entradas terminan en una salida. Ahora bien, un dato importante es que si una sola entrada es 1, el out será uno, la única manera de que out sea 0 es si todas las entradas son 0, por lo que podemos usar múltiples compuertas OR hasta reducir toda la expresión en una salida.

**Figura 17.** Representación Chip Or8Way


![Explicación Or8Way](https://i.ibb.co/BGXhqWs/Captura-de-pantalla-2024-02-15-140507.png)

**Figura 18.** Código Chip Or8Way


![Código Or8Way](https://i.ibb.co/vBwq1LK/Captura-de-pantalla-2024-02-15-140624.png)

### DMux4Way
Es un circuito lógico que toma una entrada y la dirige a uno de los cuatro posibles canales de salida, según señales de control. Tiene una entrada in, cuatro salidas a, b, c y d y dos selectores sel[0] y sel[1]. Para este circuito haremos uso de los DMux que ya tenemos.

**Figura 19.** Representación Chip DMux4Way


![Explicación DMux4Way](https://i.ibb.co/g4N38KF/Captura-de-pantalla-2024-02-15-142332.png)

**Figura 20.** Código Chip DMux4Way


![Código DMux4Way](https://i.ibb.co/DgL1nTp/Captura-de-pantalla-2024-02-15-142409.png)


### DMux8Way
Parecido al anterior solo que este cuenta con 8 salidas a, b, c, d, e, f, g, h y tres selectores sel[0] , sel[1], sel[2] lo que determina cuál de las ocho salidas se activará. Como ya tenemos el DMux4Way, vamos a usar dos y un DMux.

**Figura 20.** Código Chip DMux8Way


![Código DMux8Way](https://i.ibb.co/v1hFS4Z/Captura-de-pantalla-2024-02-15-142706.png)

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
