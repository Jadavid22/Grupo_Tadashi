## Solución de Chips

### Bit
Un bit, abreviatura de "Binary Digit" (Dígito Binario), es la unidad más básica de información en sistemas digitales y computación. Puede tener uno de dos valores posibles: 0 o 1. En esencia, representa un estado de encendido o apagado, verdadero o falso, o cualquier otra dualidad similar. Los bits son fundamentales en la representación y manipulación de datos y otros dispositivos digitales, donde combinaciones de bits se utilizan para representar números, caracteres, instrucciones de programa y otros tipos de información.

Para construirlo, podemos hacer uso de una compuerta Mux (que ya la tenemos implementada) y un DFF (Flip-Flop D):


**Figura 1.** Componentes para Construir el Bit.


![Componentes para Construir el Bit](https://i.ibb.co/Z8xvkY1/Captura-de-pantalla-2024-02-25-114916.png)

**Nota.** Imagen obtenida de: https://www.youtube.com/watch?v=lo54MEu7u9A


**Figura 2.** Código para Construir el Bit.


![Código para Construir el Bit](https://i.ibb.co/QnG8Yzw/Captura-de-pantalla-2024-02-25-131106.png)


### Register

Tiene exactamente la misma estructura que un Bit, la única diferencia es que se trata de un Array de 16 posiciones, por lo que necesitaremos 16 chips del tipo Bit.


**Figura 3.** Código para Construir el Register.


![Código para Construir el Bit](https://i.ibb.co/QNxk9dh/Captura-de-pantalla-2024-02-25-130421.png)


### PC (Program Counter)

Necesitaremos un Register, tres Mux16 (para inc, load y reset) y un incrementador para calcular todas las posibles variables

**Figura 4.** Componentes para Construir el PC.


![Componentes para Construir el PC](https://nand2tetris-hdl.github.io/img/pc.png)

**Nota.** Imagen obtenida de: https://nand2tetris-hdl.github.io/img/pc.png

**Figura 5.** Código para Construir el PC.


![Código para Construir el Bit](https://i.ibb.co/1Q3vbhs/Captura-de-pantalla-2024-02-25-155436.png)

### RAM8

Se trata de una memoria de 8 registros, cada uno de 16 bits de ancho. Out contiene el valor almacenado en la posición de memoria especificada por address. Si load==1, el valor in se carga en la posición de memoria especificada por address (el valor cargado se emitirá a out a partir del siguiente paso temporal). Vamos a utilizar un DMux8Way, 8 Register (uno para cada salida del Dmux8Way) y un Max8Way16 (para las ocho salidas de los Register).

**Figura 6.** Componentes para Construir el PC.


![Componentes para Construir el PC](https://nand2tetris-hdl.github.io/img/ram8.png)

**Nota.** Imagen obtenida de: https://nand2tetris-hdl.github.io/#reg

**Figura 7.** Código para Construir la RAM8.


![Código para Construir el Bit](https://i.ibb.co/VpfDTwt/Captura-de-pantalla-2024-02-25-161125.png)

### RAM64

Podríamos pensar que es lo mismo que la RAM8 pero con 64 Register esta vez. Pues la respuesta es no, vamos a reutilizar la RAM8 que ya tenemos.

**Figura 8.** Código para Construir la RAM64.


![Código para Construir el Bit](https://i.ibb.co/ZzQHZ9X/Captura-de-pantalla-2024-02-25-164212.png)

### RAM512

Ahora en lugar de usar la RAM8, usamos 8 de la RAM64.

**Figura 9.** Código para Construir la RAM512.


![Código para Construir el Bit](https://i.ibb.co/K2dty98/Captura-de-pantalla-2024-02-25-175732.png)


### RAM4K

Nuevamente, otros 8 chips, pero esta vez de RAM512.

**Figura 10.** Código para Construir la RAM4K.


![Código para Construir el Bit](https://i.ibb.co/Xskvs3d/Captura-de-pantalla-2024-02-25-180145.png)


### RAM16K

Finalmente, usamos en esta ocasión 4 chips de RAM4K, cambiamos el DMux8Way por un DMux4Way y el Mux8Way16 por un Mux4Way16. Finalmente modificamos los intervalos.

**Figura 11.** Código para Construir la RAM16K.


![Código para Construir el Bit](https://i.ibb.co/cy4Szdd/Captura-de-pantalla-2024-02-25-181143.png)

