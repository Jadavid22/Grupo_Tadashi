## Solución de Chips

### HalfAdder
Es un circuito lógico digital el cual hace la suma de dos números binarios de un bit. Para desarrollar el código analizamos su tabla de verdad:


**Figura 1.** Tabla de Verdad del HalfAdder.


![Componentes para Construir el Chip](https://i.ibb.co/1fM02zs/Capture.png)


Podemos observar que sum se comporta como una compuerta XOR y carry como una AND, teniendo en cuenta esto realizamos el código.

**Figura 2.** Código del HalfAdder.


![Componentes para Construir el Chip](https://i.ibb.co/pPzH0s7/Capture.png)


### FullAdder

Este circuito también es un sumador, pero de tres entradas, las dos primeras entradas (A y B) y la tercera entrada es un acarreo de entrada como C-IN. El acarreo de salida se designa como C-OUT y la salida normal se designa como S que es SUM. C-OUT se pone en alto cuando más de una entrada esta alta.

**Figura 3.** Tabla de Verdad del FullAdder.


![Componentes para Construir el Chip](https://i.ibb.co/n7DZ7zx/Capture.png)

El código es el siguiente:

**Figura 4.** Código del FullAdder.


![Componentes para Construir el Chip](https://i.ibb.co/280nSvf/Capture.png)

### Add16

Para este circuito sumamos dos entradas de 16 bits, por lo que es esencial utilizar varios chips FullAdder para ir sumando los bits de las dos entradas y el carry que se tiene se lleva a la siguiente operación.

**Figura 5.** Código del Add16.


![Componentes para Construir el Chip](https://i.ibb.co/8mNLsJQ/Capture.png)

### Inc16

Este es un incrementador de 16 bits que aumenta la entrada, la cual es un numero de 16 bits en 1. Para desarrollarlo se tomó ADD16 y una constante b cuyo primer valor se coloca como true y el resto en false.

**Figura 6.** Código del Inc.


![Componentes para Construir el Chip](https://i.ibb.co/hM2c1Qn/Capture.png)



### ALU

Es un circuito digital que realiza operaciones aritméticas como la suma o la resta además de operaciones lógicas como AND y OR. Se utilizaron MUX16 para zx y zy, la anterior con NOT para nx y ny. Para la parte aritmética un ADD, AND y otra vez MUX y por último compuertas OR y OR8WAY para zr.

**Figura 7.** Código del ALU.


![Componentes para Construir el Chip](https://i.ibb.co/zhBKzTz/Capture.png)

## Referencias

[1] https://www.geeksforgeeks.org/digital-electronics-logic-design-tutorials/?ref=lbp

[2] https://www.diariobitcoin.com/glossary/alu/

[3] https://www.youtube.com/watch?v=Wl53tFc5WYQ&list=PLu6SHDdOToSdD4-c9nZX2Qu3ZXnNFocOH&index=7

