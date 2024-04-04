## Práctica 5: Máquina Virtual, Stack Aritmético y Control Computacional ##
En esta práctica se llevará a cabo la creación de un compilador de dos niveles. Inicialmente, en el proyecto 7, se implementará la generación de código VM por parte del compilador jack para una máquina virtual. Luego, este código VM será traducido a lenguaje de máquina mediante un programa llamado traductor VM. El objetivo principal es desarrollar una versión inicial de este traductor VM, que será ampliada y perfeccionada en el proyecto 8. Ahora bien, basándonos en el trabajo realizado, en el proyecto 8 se extenderá el traductor VM para manejar comandos de bifurcación y funciones del lenguaje VM, además de añadir la capacidad de traducir programas VM que consten de múltiples archivos. Con esto, se completará el desarrollo del traductor VM, el cual posteriormente servirá como el componente backend del compilador.

### Teniendo en cuenta el marco de estas dos prácticas que son las máquinas virtuales. ¿Cuál cree que es el futuro de las máquinas virtuales?


![](https://www.muylinux.com/wp-content/uploads/2022/10/VirtualBox.jpg)


Consideramos que el futuro de las máquinas virtuales es altamente prometedor. Gracias a los proyectos realizados, podemos observar que esas herramientas demuestran la eficacia y la versatilidad en la generación de código y la traducción entre diferentes niveles de lenguaje. La implementación de un compilador de dos niveles abre nuevas oportunidades para la optimización y la portabilidad del software. En el proyecto 7, la elaboración de un compilador jack capaz de generar código VM proporciona una capa de abstracción fundamental para el desarrollo de software. Además, la separación del código fuente del lenguaje de alto nivel del código de máquina ofrece flexibilidad y facilita la portabilidad. Por otro lado, el proyecto 8 lleva esta idea un paso más allá al extender el traductor VM para manejar comandos de bifurcación y funciones del lenguaje VM, así como la capacidad de traducir programas VM multi-archivo. Esta ampliación no solo mejora la funcionalidad del traductor VM, sino que también facilita el proceso para la creación de compiladores más robustos y eficientes. Con estas herramientas, se abre un horizonte prometedor para la creación de software más sofisticado, portable y fácil de mantener en el futuro.

### ¿Cuál es la principal similitud entre un contenedor y una máquina virtual?


![](https://i0.wp.com/juancarlossaavedra.me/wp-content/uploads/2017/03/vmvscont.png)


Una de las similitudes más notables entre los contenedores y las máquinas virtuales es su capacidad para proporcionar entornos de ejecución aislados y portátiles. Tanto los contenedores como las máquinas virtuales permiten encapsular las aplicaciones y sus dependencias en un entorno virtual, haciéndolas independientes del sistema operativo y del hardware subyacente. Esta característica es esencial para implementar soluciones de computación en la nube donde la portabilidad y la escalabilidad son esenciales. Además, tanto los contenedores como las máquinas virtuales brindan soluciones eficientes para la gestión de recursos y la distribución de cargas de trabajo en entornos de infraestructura de TI. Ambos permiten que se ejecuten múltiples aplicaciones en un único servidor físico, maximizando la utilización de recursos y simplificando la administración y la implementación de aplicaciones.

## Bonus: ¿Cual es la ventaja del contenedor respecto a la máquina virtual?

Una de las ventajas radica en su eficiencia y velocidad. Los contenedores comparten el kernel del sistema operativo del host, lo que significa que no hay necesidad de ejecutar múltiples sistemas operativos completos, como sí ocurre con las máquinas virtuales. Esta característica reduce significativamente los requisitos de recursos y el tiempo de inicio de los contenedores en comparación con las máquinas virtuales. Además, los contenedores son más livianos, ya que no tienen la sobrecarga asociada con la emulación de hardware de una máquina virtual. Esto los hace ideales para despliegues a gran escala y para aplicaciones que requieren un alto grado de movilidad y flexibilidad.
Otra ventaja importante, como ya hemos mencionado, es su portabilidad. Los contenedores encapsulan no solo la aplicación, sino también todas sus dependencias y bibliotecas necesarias para su ejecución. Esto garantiza que una aplicación empaquetada en un contenedor se ejecute de manera consistente en cualquier entorno que admita contenedores, independientemente del sistema operativo usado.

## Referencias ##
[1] https://www.muylinux.com/wp-content/uploads/2022/10/VirtualBox.jpg

[2] https://i0.wp.com/juancarlossaavedra.me/wp-content/uploads/2017/03/vmvscont.png
