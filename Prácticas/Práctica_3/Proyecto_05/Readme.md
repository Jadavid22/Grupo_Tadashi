## Solución de Chips

### Memory
Hace alusión a la memoria RAM, componente crucial en las computadoras y dispositivos electrónicos que actúa como el espacio de trabajo del procesador. Permite almacenar y acceder a datos e instrucciones de manera rápida y temporal mientras el dispositivo está encendido. En el modelo de Von Neumann, la memoria principal es donde se almacena la información y los programas que la unidad central de procesamiento (CPU) utiliza para realizar cálculos y ejecutar programas.


**Figura 1.** Funcionamiento y Comunicación de la Memoria con los demás Componentes

![Componentes para Construir el Bit](https://i.ibb.co/NjYV4Dg/memory1-funcionamiento-y-comunicacion-de-la-memoria-con-otros-componentes.png)


Para implementar el espacio de direcciones completo de la memoria de datos de Hack, incluyendo RAM, pantalla mapeada en memoria y teclado mapeado en memoria, tenemos lo siguiente:

- **Entradas:**

  - **in[16]:** Entrada de datos de 16 bits que se cargará en la memoria si "load" está activo.
  - **load:** Señal de control que indica si se debe cargar un valor en la memoria en la dirección especificada.
  - **address[15]:** Dirección de memoria de 15 bits que especifica la ubicación a la que se accede en la memoria.

- **Salidas:**
  - **out[16]:** Valor de la memoria en la dirección especificada por "address".

- **Componentes internos (PARTS):**
  - **DMux4Way:** Desmultiplexor que selecciona una de las cuatro salidas basándose en dos bits de selección. En este caso, se utiliza para seleccionar entre RAM, pantalla y teclado basándose en los bits 13 y 14 de la dirección.
  - **Or:** Operación lógica OR que combina las señales de control para la RAM.
  - **RAM16K:** Chip de RAM de 16K que almacena y recupera datos basándose en la dirección y la señal de carga.
  - **Screen:** Chip que implementa la memoria mapeada en pantalla y que almacena y recupera datos basándose en la dirección y la señal de carga.
  - **Keyboard:** Chip que implementa la memoria mapeada en teclado y que almacena y recupera datos basándose en la dirección y la señal de carga.
  - **Mux4Way16:** Multiplexor que selecciona una de las cuatro entradas de 16 bits basándose en dos bits de selección. En este caso, se utiliza para seleccionar entre los valores de RAM, pantalla y teclado basándose en los bits 13 y 14 de la dirección.


**Figura 2.** Código de Memory que se va a Implementar

![Componentes para Construir el Bit](https://i.ibb.co/8xWcGVV/memory2-codigo-implementado.png)


El resultado consiste en comprobar si después de presionar la letra K en la opción del Keyboard, en la pantalla se muestran dos rayas horizontales. Posteriormente, se presiona Y para confirmar que todo está bien.


**Figura 3.** Resultado en Hardware Simulator al Seguir los Pasos de Comprobación

![Componentes para Construir el Bit](https://i.ibb.co/qR5g16H/memory3-resultado-hardware-simulator-al-seguir-los-pasos-de-comprobacion.png)


### CPU

Es el componente principal de una computadora y otros dispositivos que procesa instrucciones y realiza cálculos. A menudo se le llama el “cerebro” del dispositivo porque controla todas las funciones y ejecuta los programas, recibe datos de la memoria RAM, los procesa y luego devuelve los resultados. Es fundamental para cualquier dispositivo con capacidad de procesamiento de datos. En cuanto al funcionamiento como tal en código, esta sería una forma de implementar la CPU:

- **Entradas:**

  - **inM[16]:** Valor de entrada M (M = contenido de RAM[A]).
  - **instruction[16]:** Instrucción binaria a ejecutar.
  - **reset:** Señal que indica si se debe reiniciar el programa actual (reset==1) o continuar ejecutando el programa actual (reset==0).

- **Salidas:**
  - **outM[16]:** Valor de salida M.
  - **writeM:** Indica si se debe escribir en M.
  - **addressM[15]:** Dirección en la memoria de datos (de M).
  - **pc[15]:** Dirección de la siguiente instrucción.

- **Componentes internos (PARTS):**
  - **Mux16:** Multiplexor de 16 bits que selecciona una de las entradas basándose en el bit de selección en la posición 15 de la instrucción. Las salidas seleccionadas son campos específicos de la instrucción que se utilizarán para controlar otras partes.
  - **ALU:** Unidad lógica y aritmética que realiza operaciones lógicas y aritméticas en los valores de entrada x e y, según los campos de control cAluZx, cAluNx, cAluZy, cAluNy, cAluF, y cAluNo. La salida se almacena en aluOut y se copia en outM.
  - **Or, Not, And:** Operaciones lógicas.
  - **Mux16 (2):** Multiplexores adicionales para seleccionar entre las entradas instruction y aluOut basándose en el tipo de instrucción (cType) y entre aRegOut e inM basándose en cAOrM.
  - **ARegister, DRegister:** Registros para almacenar valores. ARegister se utiliza para almacenar la dirección de memoria actual (aRegOut), y DRegister para almacenar el resultado de la ALU (aluOut).
  - **PC:** Contador de programa que almacena la dirección de la siguiente instrucción. Se carga con aRegOut si jump es verdadero, se incrementa si inc es verdadero, y se reinicia a 0 si reset es verdadero.


**Figura 4.** Código de CPU que se va a Implementar

![Componentes para Construir el Bit](https://i.ibb.co/c24b3kL/cpu1-codigo-que-se-va-a-implementar.png)


Para verificar el funcionamiento, solo cargamos en el Hardware Simulator el archivo CPU.hdl y lo comparamos con CPU.tst


**Figura 5.** Comprobar el Funcionamiento en el Hardware Simulator

![Componentes para Construir el Bit](https://i.ibb.co/sbZSxM1/cpu2-comprobacion-del-funcionamiento-en-el-hardware-simulator.png)


### Computer

**Figura 5.** 

![Componentes para Construir el Bit]()

## Referencias

[1] https://www.eldiario.es/tecnologia/diario-turing/john-neumann-revolucionando-computacion-manhattan_1_2705516.html


[2] https://softwarelab.org/es/blog/que-es-una-cpu/


[3] https://www.youtube.com/watch?v=7Np0-fUYaC8


[4] https://www.youtube.com/watch?v=xHh2GdJl4Cs&t=2360s
