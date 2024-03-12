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


**Figura 4.** Cargar Mult.asm y Generar Mult.hack

![Componentes para Construir el Bit](https://i.ibb.co/cwxRnqd/Mult-4-Traducci-n-y-Creaci-n-del-Hack.png)


Finalmente, cargamos en el CPUEmulator.bat el archivo Mult.hack para corroborar que el resultado es el correcto. En nuestro caso vamos a hacer la multiplicación de 5*5=25, entonces los valores en la RAM deberían quedar así:

- RAM[0]=5
- RAM[1]=5
- RAM[2]=25


**Figura 5.** Prueba de Resultados en el CPUEmulator.bat

![Componentes para Construir el Bit](https://i.ibb.co/ySgXyr0/1.png)


### Fill

Este programa implementa un bucle infinito que escucha la entrada del teclado. Cuando se presiona una tecla, el programa pinta la pantalla de negro (escribiendo "1" en cada píxel); la pantalla permanece completamente negra mientras se mantiene presionada la tecla. Cuando no se presiona ninguna tecla, el programa borra la pantalla, es decir, escribe "0" en cada píxel; la pantalla permanece completamente blanca mientras no se presiona ninguna tecla.

Para su implementación en código seguiremos los siguientes pasos:

- **(RESTART):** Inicializa la dirección base de la pantalla en la dirección de memoria RAM[0]. Esto se hace para poder manipular fácilmente la pantalla en los bucles posteriores.

- **(KBDCHECK):** Esta sección del código verifica si se ha presionado una tecla. Para hacerlo, carga el valor actual del teclado en el registro D. Si D es mayor que cero (es decir, si se ha presionado una tecla), el programa salta a la etiqueta BLACK para ennegrecer la pantalla. Si D es igual a cero, significa que no se ha presionado ninguna tecla, por lo que el programa salta a la etiqueta WHITE para blanquear la pantalla.

- **(BLACK):** En esta parte, el programa prepara la pantalla para ser ennegrecida. Esto se logra colocando el valor -1 en la dirección base de la pantalla. El valor -1 en binario representa todos los bits establecidos en 1, lo que en la pantalla significa píxeles de color negro.

- **(WHITE):** Aquí, el programa prepara la pantalla para ser blanqueada. Esto se logra colocando el valor 0 en la dirección base de la pantalla. El valor 0 en binario representa todos los bits establecidos en 0, lo que en la pantalla significa píxeles de color blanco.

- **(CHANGE):** Esta sección del código decide si se debe seguir ennegreciendo o blanqueando la pantalla. Si el valor en la dirección base de la pantalla es mayor que cero, significa que aún hay píxeles por ennegrecer, por lo que el programa vuelve a la etiqueta RESTART para continuar ennegreciendo la pantalla. Si el valor es igual a cero, significa que todos los píxeles ya están en negro y el programa reinicia el ciclo, volviendo a comprobar si se ha presionado alguna tecla para cambiar la pantalla a blanco.


**Figura 6.** Código RESTART y KBDCHECK

![Componentes para Construir el Bit](https://i.ibb.co/DkxSfyy/fill-1-codigo-restart-y-kbdcheck.png)


**Figura 7.** Código BLACK, WHITE y CHANGE

![Componentes para Construir el Bit](https://i.ibb.co/TqrYDdd/fill-2-codigo-black-white-y-change.png)

De manera similar como hicimos en el Mult.asm, cargamos nuestro archivo Fill.asm en el Assembler.bat para traducir y generar el HACK en la misma ruta del proyecto.

**Figura 8.** Cargar Fill.asm y Generar Fill.hack

![Componentes para Construir el Bit](https://i.ibb.co/pRf49DB/fill-6-generar-archivo-hack.png)

Para finalizar, en el CPUEmulator.bat verificamos si al cargar y ejecutar el archivo Fill.hack la pantalla se hace negra al dejar presionada alguna tecla y vuelve a ser blanca al momento de soltarla.

**Figura 9.** Screen Cuando no hay Tecla Presionada

![Componentes para Construir el Bit](https://i.ibb.co/TYTQ8xj/fill-7-pantalla-cuando-no-hay-tecla-presionada.png)

**Figura 10.** Screen Cuando sí hay Tecla Presionada

![Componentes para Construir el Bit](https://i.ibb.co/9WYwZMz/fill-8-pantalla-cuando-si-hay-tecla-presionada.png)
