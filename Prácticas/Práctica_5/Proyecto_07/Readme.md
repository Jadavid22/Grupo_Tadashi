## Traductor Simple de Lenguaje de Máquina Virtual (VM) a Código Ensamblador (ASM)
El archivo .py implementa un traductor simple de un lenguaje de máquina virtual (VM) a código ensamblador (ASM). Este tipo de conversiones con comunes en el desarrollo de compiladores y emuladores de sistemas informáticos. Así pues, en este caso el traductor toma como entrada archivos en formato VM (SimpleAdd, StackTest, BasicTest, PointerTest y StaticTest) y genera archivos ASM correspondientes que pueden ser ensamblados y ejecutados en una arquitectura específica.

El traductor maneja varias operaciones básicas como push, pop, operaciones aritméticas, lógicas y de comparación. Cada operación se traduce en instrucciones ASM que manipulan la pila y realizan las operaciones necesarias. De igual forma, se utilizan etiquetas para controlar el flujo de ejecución en operaciones de salto condicional.

### Explicación del Código
- **Definición de la función traductorVM(archivo):** La función traductorVM toma un nombre de archivo de entrada en formato VM y genera un archivo ASM correspondiente.
- **Apertura del archivo de salida:** Se crea un nuevo archivo con extensión .asm para escribir el código traducido. El nombre del archivo de salida se deriva del nombre del archivo de entrada.
- **Inicialización de una variable k:** La variable k se utiliza para generar etiquetas únicas para las operaciones de comparación (eq, gt, lt).
- **Bucle for para procesar cada línea del archivo de entrada:** El bucle recorre cada línea del archivo de entrada y la procesa.
- **Manejo de instrucciones push:** Para instrucciones push, se obtienen el segmento y el valor, y se escriben las instrucciones ASM correspondientes para colocar el valor en la pila.
- **Manejo de instrucciones pop:** Para instrucciones pop, se obtienen el segmento y el valor, y se escriben las instrucciones ASM correspondientes para sacar el valor de la pila y almacenarlo en la posición correcta.
- **Manejo de operaciones aritméticas:** Las operaciones add y sub suman o restan los dos últimos valores de la pila. La operación neg cambia el signo del último valor en la pila.
- **Manejo de operaciones de comparación (eq, gt, lt):** Se utilizan etiquetas únicas (True1, False1, True2, etc.) para controlar el flujo de ejecución después de las comparaciones.
- **Manejo de operaciones lógicas (and, or, not):** Las operaciones and y or realizan las operaciones lógicas correspondientes en los dos últimos valores de la pila. La operación not realiza la operación lógica not en el último valor de la pila.
- **Escritura en el archivo de salida:** Después de procesar cada línea, se escriben las instrucciones ASM correspondientes en el archivo de salida.
**Llamadas a traductorVM() para cada archivo VM:** Se realizan llamadas a la función traductorVM() para cada archivo VM que se quiere traducir a ASM.

  ## Referencias

[1] https://github.com/Mirr1s/tech.github.io/tree/main/Pr%C3%A1cticas/Pr%C3%A1ctica%205/Projecto%207%20-%20VM%201%20Stack%20Arithmetic


[2] https://www.youtube.com/watch?v=vj1veGsRdbw


[3] https://www.youtube.com/watch?v=49Ct7CAOlss


[4] https://github.com/6HJS/Nand2Tetris-VMTranslator
