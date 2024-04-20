## Shooting Game
El juego es una versión simplificada del Space Invaders: aquí tenemos un objetivo que se va a ir movimiento verticalmente y cuando el usuario presione la barra espaciadora la pistola disparará un proyectil. Si este alcanza el objetivo su puntuación aumenta y al final se le muestra el score total al jugador.

**Figura 1.** Juego Funcionando en el Simulador de la Máquina Virtual (VM)


![](https://i.ibb.co/NSH3VKN/Juego-Funcionando-en-el-Simulador-de-la-M-quina-Virtual-VM.png)


**Figura 2.** Preguntar al Usuario si Desea Reiniciar la Partida


![](https://i.ibb.co/3vkN07Q/Preguntar-al-Usuario-si-Desea-Reiniciar-la-Partida.png)


**Figura 3.** Sistema de Puntuación Sencillo Basado en el Total de Aciertos


![](https://i.ibb.co/WnX07gx/Sistema-de-Puntuaci-n-Sencillo-Basado-en-el-Total-de-Aciertos.png)

## Funcionamiento

A continuación, dejamos una descripción de cómo funcionan las clases y cómo interactúan entre sí para hacer funcionar el juego:

### Clase Target (Objetivo): 
Representa el objetivo que el jugador intenta golpear en el juego. Tiene varios campos para almacenar la posición y la puntuación, así como la velocidad a la que se mueve.

- **position:** Posición actual del objetivo en la pantalla.
- **result:** Puntuación total acumulada por el jugador.
- **score:** Puntuación obtenida en el último disparo.
- **opportunity:** Número de oportunidades restantes para el jugador.
- **velocity:** Velocidad a la que se mueve el objetivo.

El constructor de la clase Target inicializa estos campos y recibe un parámetro speed   que establece la velocidad del objetivo. A su vez, contiene los siguientes métodos:
  
- **render_objective(boolean color):** Dibuja el objetivo en la pantalla en una posición específica. El color del mismo se determina por el parámetro color.
- **navigate(Gun weapon):** Controla el movimiento del objetivo que se desplaza hacia arriba y hacia abajo en la pantalla. Si el proyectil lo golpea, se calcula la puntuación y se actualiza la puntuación total.
- **absolute(int a, int b):** Devuelve el valor absoluto de la diferencia entre a y b.
- **compute_score():** Calcula la puntuación basada en qué tan cerca está el disparo del centro del objetivo.
- **descend():** Mueve el objetivo hacia abajo en la pantalla.
- **ascend():** Mueve el objetivo hacia arriba en la pantalla.
- **display_score():** Muestra la puntuación actual, las balas restantes y la puntuación total en la pantalla.
- **display_final():** Muestra la puntuación total final en la pantalla.
- **remove():** Hace desaparecer el objetivo y libera la memoria que ocupaba.

### Clase Main (Principal): 

Controla el flujo del juego, creando y controlando las instancias de las clases Gun y Target, y gestionando la interacción del jugador con el juego.

- **Gun weapon, Target objective, boolean marker, int velocity, boolean active_game, int y retry:** Estas son las variables que se utilizan en el juego. weapon es una instancia de la clase Gun que representa el arma que dispara el proyectil. objective es una instancia de la clase Target que representa el objetivo que el jugador intenta golpear. marker es una variable booleana que se utiliza para controlar los bucles en el juego. velocity es la velocidad del objetivo y del proyectil. active_game es una variable booleana que determina si el juego está activo o no. retry es una variable que se utiliza para determinar si el jugador quiere jugar de nuevo o no.
- **let active_game = true**: Establece que el juego está activo al principio.
- **while (active_game) {...}:** Bucle principal del juego. Mientras el juego esté activo, este bucle seguirá ejecutándose.
- **let marker = true; while (marker) {...}:** Bucle que permite al jugador elegir un nivel de dificultad entre fácil (1), medio (2) y difícil (3). La velocidad del objetivo y del proyectil se determina en función de la dificultad elegida.
- **let velocity = 6 / velocity:** Establece la velocidad del objetivo y del proyectil en función de la dificultad elegida.
- **let objective = Target.new(velocity):** Crea una nueva instancia de la clase Target con la velocidad especificada.
- **do objective.display_score():** Muestra la puntuación actual en la pantalla.
- **let weapon = Gun.new(0,0,(velocity)):** Crea una nueva instancia de la clase Gun con la velocidad especificada.
- **do objective.render_objective(true):** Dibuja el objetivo en la pantalla.
- **do objective.navigate(weapon):** Mueve el objetivo en la pantalla y controla el disparo del proyectil.
- **do Screen.clearScreen():** Esto limpia la pantalla.
- **do objective.display_final():** Esto muestra la puntuación final en la pantalla.
- **do Sys.wait(1000):** Hace una pausa en el juego durante 1000 milisegundos.
- **if (~(retry=1)) {...}:** Si el usuario decide no jugar de nuevo, se muestra un mensaje de despedida y el juego termina.

### Clase Gun (Arma): 

Responsable de representar y controlar el arma en el juego, incluyendo el disparo del proyectil y la detección de si el proyectil ha golpeado el objetivo.

- **field int x, y; field Bullet bullet; field int speed:** Campos de la clase. x y y representan la posición del arma en la pantalla. bullet es una instancia de la clase Bullet que representa el proyectil que dispara el arma. speed es la velocidad a la que se dispara el proyectil.
- **constructor Gun new(int Ax, int Ay, int Aspeed) {...}:** Constructor de la clase. Inicializa los campos x, y, y speed con los valores pasados como parámetros. También crea una nueva instancia de la clase Bullet y la asigna al campo bullet. Finalmente, dibuja el arma en la pantalla.
- **method void draw_gun() {...}:** Dibuja el arma en la pantalla. Utiliza el método drawRectangle de la clase Screen para dibujar varias partes a la vez.
- **method void fire_start(int location) {...}:** Inicia el disparo del proyectil. Utiliza el método poke de la clase Memory para escribir varios valores en la memoria, creando una animación de disparo. Luego, espera un corto período de tiempo y borra la animación de la pantalla.
- **method void fire() {...}:** Dispara el proyectil, llamando al método navigate del proyectil.
- **method void blast(int address) {...}:** Este método se invoca cuando el proyectil golpea el objetivo, causando una explosión. Llama al método explode del proyectil.
- **method boolean hit() {...}:** Determina si el proyectil ha golpeado el objetivo. Llama al método impact del proyectil.
- **method void disappear() {...}:** Hace desaparecer el proyectil cuando golpea el objetivo. Llama al método vanish del proyectil.
- **method void dispose() {...}:** Libera la memoria que ocupaba el arma cuando ya no se necesita.

### Clase Bullet (Proyectil):
Responsable de representar y controlar el proyectil en el juego, incluyendo su movimiento, la detección de si ha golpeado el objetivo, y la creación de una animación de explosión cuando golpea el objetivo.

- **field int velocity; field int position:** Campos de la clase. velocity es la velocidad a la que se dispara el proyectil y position es la posición actual del proyectil en la pantalla.
- **constructor Bullet new(int speed) {...}:** Constructor de la clase. Inicializa los campos position y velocity con los valores pasados como parámetros.
- **method void render_projectile() {...}:** Dibuja el proyectil en la pantalla en una posición específica.
- **method void navigate() {...}:** Este método mueve el proyectil a lo largo de una línea en la pantalla. Si el proyectil aún no ha alcanzado el final de la misma, lo borra de su posición actual, actualiza la posición y luego dibuja el proyectil en la nueva posición.
- **method void vanish() {...}:** Hace desaparecer el proyectil cuando golpea el objetivo, lo borra de la pantalla y luego llama al método remove() para liberar la memoria que ocupaba.
- **method void explode(int location) {...}:** Este método se invoca cuando el proyectil golpea el objetivo, causando una explosión. Utiliza el método poke de la clase Memory para escribir varios valores en la memoria, creando una animación de explosión. Luego, espera un corto período de tiempo y borra la animación.
- **method boolean impact() {...}:** Determina si el proyectil ha golpeado el objetivo. Devuelve true si el proyectil ha alcanzado el final de la pantalla, y false en caso contrario.
- **method void remove() {...}:** Libera la memoria que ocupaba el proyectil cuando ya no se necesita.
  
Estas clases trabajan juntas para crear el juego. La clase main controla el flujo del juego y utiliza las clases gun y target para representar los elementos del juego. El target se mueve de arriba a abajo en la pantalla y el jugador utiliza el gun para disparar proyectiles al target. Cuando uno de estos lo golpea, el jugador recibe puntos basados en qué tan cerca estaba el proyectil del centro del target. El juego continúa hasta que el jugador decide dejar de jugar o hasta que se le acaban los intentos.

## Referencias

[1] https://yizhe87.medium.com/from-nand-to-tetris-nand2tetris-project-9-fcaabcd17f5b
