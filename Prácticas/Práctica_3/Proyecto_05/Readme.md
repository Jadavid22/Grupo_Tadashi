## Solución de Chips

### Memory
Hace alusión a la memoria RAM, componente crucial en las computadoras y dispositivos electrónicos que actúa como el espacio de trabajo del procesador. Permite almacenar y acceder a datos e instrucciones de manera rápida y temporal mientras el dispositivo está encendido. En el modelo de Von Neumann, la memoria principal es donde se almacena la información y los programas que la unidad central de procesamiento (CPU) utiliza para realizar cálculos y ejecutar programas.


**Figura 1.** Funcionamiento y Comunicación de la Memoria con los demás Componentes

![Componentes para Construir el Bit](https://i.ibb.co/NjYV4Dg/memory1-funcionamiento-y-comunicacion-de-la-memoria-con-otros-componentes.png)


Para implementar el espacio de direcciones completo de la memoria de datos de Hack, incluyendo RAM, pantalla mapeada en memoria y teclado mapeado en memoria, tenemos lo siguiente:

- **Entradas:**

  - in[16]: Entrada de datos de 16 bits que se cargará en la memoria si "load" está activo.
  - load: Señal de control que indica si se debe cargar un valor en la memoria en la dirección especificada.
  - address[15]: Dirección de memoria de 15 bits que especifica la ubicación a la que se accede en la memoria.

- **Salidas:**
  - out[16]: Valor de la memoria en la dirección especificada por "address".

- **Componentes internos (PARTS):**
  - DMux4Way: Desmultiplexor que selecciona una de las cuatro salidas basándose en dos bits de selección. En este caso, se utiliza para seleccionar entre RAM, pantalla y teclado basándose en los bits 13 y 14 de la dirección.
  - Or: Operación lógica OR que combina las señales de control para la RAM.
  - RAM16K: Chip de RAM de 16K que almacena y recupera datos basándose en la dirección y la señal de carga.
  - Screen: Chip que implementa la memoria mapeada en pantalla y que almacena y recupera datos basándose en la dirección y la señal de carga.
  - Keyboard: Chip que implementa la memoria mapeada en teclado y que almacena y recupera datos basándose en la dirección y la señal de carga.
  - Mux4Way16: Multiplexor que selecciona una de las cuatro entradas de 16 bits basándose en dos bits de selección. En este caso, se utiliza para seleccionar entre los valores de RAM, pantalla y teclado basándose en los bits 13 y 14 de la dirección.


**Figura 2.** Código que se va a Implementar

![Componentes para Construir el Bit](https://i.ibb.co/8xWcGVV/memory2-codigo-implementado.png)


El resultado consiste en comprobar si después de presionar la letra K en la opción del Keyboard, en la pantalla se muestran dos rayas horizontales. Posteriormente, se presiona Y para confirmar que todo está bien.


**Figura 3.** Resultado en Hardware Simulator al Seguir los Pasos de Comprobación

![Componentes para Construir el Bit](https://i.ibb.co/qR5g16H/memory3-resultado-hardware-simulator-al-seguir-los-pasos-de-comprobacion.png)


### CPU

### Computer

**Figura 4.** 

![Componentes para Construir el Bit]()

## Referencias

[1] https://www.eldiario.es/tecnologia/diario-turing/john-neumann-revolucionando-computacion-manhattan_1_2705516.html


[2] https://softwarelab.org/es/blog/que-es-una-cpu/


[3] https://www.youtube.com/watch?v=7Np0-fUYaC8


[4] https://www.youtube.com/watch?v=xHh2GdJl4Cs&t=2360s
