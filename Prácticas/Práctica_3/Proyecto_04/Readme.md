## Lenguaje Ensamblador ##

### Mult

El objetivo principal de este programa es multiplicar dos números enteros no negativos y almacenar el resultado en una ubicación de memoria específica. A continuación, tendremos una breve explicación por pasos de cómo lo desarrolla la maquina en el funcionamiento del programa Mult.asm:

- **Inicialización:** El programa comienza inicializando un contador llamado "i" en 1, que se utilizará para iterar a través de los bits del multiplicador.
- **Inicialización del resultado:** Inicializa la ubicación de memoria RAM[2] (R2) a 0, donde se almacenará el resultado final de la multiplicación.
- **Bucle de multiplicación:** El programa entra en un bucle principal etiquetado como "LOOP". En cada iteración de este bucle, se realiza una multiplicación parcial de los números.
- **Comparación de los números:** El programa compara los números multiplicador (R1) y multiplicando (R0). Dependiendo de si el multiplicador es mayor o menor que el multiplicando, el programa ejecuta diferentes secciones de código para manejar los casos respectivos.
- **Multiplicación parcial:** En cada iteración, el programa realiza una multiplicación parcial. Si el bit actual del multiplicador es 1, suma el multiplicando al resultado parcial almacenado en R2.
- **Desplazamiento de bits:** Después de cada iteración, el programa realiza un desplazamiento a la izquierda del multiplicando y un desplazamiento a la derecha del multiplicador. Esto es esencial para realizar la multiplicación bit a bit.
- **Fin del bucle de multiplicación:** El bucle "LOOP" continúa hasta que se han multiplicado todos los bits del multiplicador.
- **Fin del programa:** Una vez que se ha completado la multiplicación, el programa termina y el resultado final se almacena en la ubicación de memoria RAM[2].


**Figura 1.** Inicialización y Código del LOOP.

![Componentes para Construir el Bit](https://i.ibb.co/pzNSLBw/Mult-1-Inicializaci-n-y-LOOP.png)


**Figura 2.** Código del LESS.

![Componentes para Construir el Bit](https://i.ibb.co/phZ4m3f/Mult-2-LESS.png)


**Figura 3.** Código del GREATER y END.

![Componentes para Construir el Bit](https://i.ibb.co/FmRYcCy/Mult-3-GREATER-y-END.png)


Posteriormente, cargamos nuestro archivo Mult.asm en el Assembler.bat para traducir y generar el HACK en la misma ruta del proyecto.


**Figura 4.** Cargar Mult.asm y Generar Mult.hack.

![Componentes para Construir el Bit](https://i.ibb.co/cwxRnqd/Mult-4-Traducci-n-y-Creaci-n-del-Hack.png)


Finalmente, comparamos en el CPUEmulator.bat el archivo Mult.asm y Mult.tst para corroborar que la implementación esté bien hecha.


**Figura 5.** Comparación y Prueba de Resultados en el CPUEmulator.bat.

![Componentes para Construir el Bit](https://i.ibb.co/gdWfhpH/Mult-5-Comparacion-en-el-CPU-Emulator.png)
