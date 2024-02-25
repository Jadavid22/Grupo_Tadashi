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



