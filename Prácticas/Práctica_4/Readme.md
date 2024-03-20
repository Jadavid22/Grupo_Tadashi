## Práctica 4: Desarrollo de un Ensamblador para Interpretar Lenguaje de Máquina HACK ##

En el presente proyecto se implementa un código de lenguaje ensamblador, que es un tipo de programa de bajo nivel escrito en lenguaje de máquina simbólico, para traducir los programas escritos en lenguaje ensamblador simbólico a código binario.

### Teniendo en cuenta las características del ensamblador, ¿Cuál es la principal limitante que observan? Justifique su respuesta.

La principal limitación observada es la falta de abstracción y las comodidades modernas que se encuentran en los lenguajes de programación de nivel superior.
- ¿Falta de Abstracción? el ensamblador trabaja directamente con la arquitectura de la computadora y sus instrucciones detalladas. Esto significa que el programador debe tener un conocimiento detallado de la arquitectura subyacente y las instrucciones de la máquina, lo que puede hacer que la codificación sea más propensa a errores y menos intuitiva que en otros lenguajes de nivel superior. De igual forma, se debe  gestionar la asignación y liberación de memoria manualmente, lo que puede provocar errores y complicar la creación de programas más complejos. Además, se presentan algunas limitaciones de legibilidad y mantenibilidad debido a la naturaleza detallada y específica del lenguaje ensamblador, pues los programas suelen ser más difíciles de leer y mantener que los programas escritos en lenguajes de nivel superior, lo que puede dificultar la interoperabilidad y el mantenimiento a largo plazo.


Ahora bien, a pesar de estas limitaciones, el uso de un ensamblador también ofrece beneficios como un mejor control del hardware y la capacidad de optimizar el rendimiento del programa para situaciones específicas. Sin embargo, es importante comprender que trabajar con lenguaje ensamblador tiene un mayor nivel de complejidad y detalle que programar en lenguajes de programación de nivel superior.


## Bonus ##

### ¿Por qué es tan importante el ensamblador?

Porque gracias a él tenemos a nuestro alcance características como:

- **Control de bajo nivel:** Tener control preciso sobre el hardware de la computadora. Las instrucciones se ejecutan directamente en la unidad central de procesamiento (CPU). Esto es fundamental para tareas específicas que requieren una interacción cercana con el hardware.
- **Eficiencia:** El código ensamblador es altamente eficiente y rápido. No hay capas de abstracción que ralenticen la ejecución del programa, como ocurre en los lenguajes de alto nivel. Esto es especialmente importante en sistemas donde cada ciclo de CPU cuenta, como en sistemas embebidos o sistemas operativos.
- **Arquitectura específica:** Cada arquitectura de procesador tiene su propio lenguaje ensamblador, definido por el fabricante de hardware. Esto significa que el lenguaje ensamblador es específico de una arquitectura de computadora en particular. A diferencia de los modernos lenguajes de programación de alto nivel, no puedes usar lenguaje ensamblador independientemente de la arquitectura en la que fue desarrollado el dispositivo.
- **Comprensión profunda del hardware:** Programar en lenguaje ensamblador requiere un conocimiento profundo del hardware y la arquitectura de la computadora. Los programadores deben entender cómo funcionan los registros, las instrucciones de la CPU y las posiciones de memoria. Esto fomenta una comprensión más completa del sistema.

## Implementación del Ensamblador

El código realiza un ensamblado de un programa en lenguaje ensamblador de Hack a código máquina de 16 bits, utilizando tablas y diccionarios para manejar los símbolos y las instrucciones, y escribiendo el resultado en un archivo .hack para su uso en la plataforma Hack.

- **Diccionarios de mapeo:** Los diccionarios comp_dict, dest_dict y jump_dict son utilizados para mapear los mnemónicos de las instrucciones de Hack a sus códigos binarios correspondientes. Por ejemplo, el mnemónico D=A+1 se traduce a comp_dict["D+A"] = "1000010". Estos diccionarios facilitan la traducción de las instrucciones ensamblador a código máquina.****
- **Tabla de símbolos predefinidos:** La tabla symbol_table contiene los símbolos predefinidos en el lenguaje ensamblador de Hack, como las direcciones de memoria RAM especiales (SP, LCL, ARG, THIS, THAT), las posiciones de pantalla y teclado (SCREEN, KBD), y los registros generales (R0-R15). Esta tabla se utiliza para asignar direcciones de memoria a estos símbolos cuando se encuentran en el código.
- **Primera pasada:** En la primera pasada por el archivo de entrada, se procesan las etiquetas (por ejemplo, (LOOP)) y se agregan a la tabla de símbolos con su dirección de memoria correspondiente. También se incrementa la dirección de memoria para las instrucciones que no son etiquetas.
- **Segunda pasada:** En la segunda pasada por el archivo de entrada, se traducen las instrucciones a código máquina. Las instrucciones de dirección A (@) se traducen directamente a código binario, ya sea como una dirección de memoria o como un valor constante. Las instrucciones de computación (comp) se traducen usando los diccionarios de mapeo (comp_dict, dest_dict, jump_dict) para obtener los códigos binarios correspondientes a cada parte de la instrucción.
- **Escritura en archivo de salida:** En lugar de imprimir el código máquina por la terminal, se escribe en un archivo de salida con extensión .hack. Cada instrucción se escribe en una línea separada en el archivo de salida, lo que permite almacenar el código máquina generado para su uso posterior en la plataforma Hack.

## Referencias ##

[1] https://historiadelaempresa.com/que-es-el-lenguaje-ensamblador


[2] https://www.educaopen.com/digital-lab/blog/software/lenguaje-ensamblador


[3] https://es.wikipedia.org/wiki/Lenguaje_ensamblador


[4] https://lovtechnology.com/que-son-los-lenguajes-ensambladores-como-funcionan-y-para-que-sirven/

[5] https://www.tecnologia-informatica.com/el-lenguaje-ensamblador/
