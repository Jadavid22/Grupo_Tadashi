// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed.
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.

(RESTART)

@SCREEN
D=A
@0
M=D	//Coloca el inicio de la pantalla en RAM[0].

///////////////////////////

(KBDCHECK)

@KBD
D=M
@BLACK
D;JGT	//Si se presiona alguna tecla, pone negra la pantalla.
@WHITE
D;JEQ	//De lo contrario blanquea la pantalla.

@KBDCHECK

0;JMP

(BLACK)

@1
M=-1	//Con lo que se rellena la pantalla en el caso de que se presione tecla (-1=11111111111111).
@CHANGE
0;JMP

(WHITE)

@1
M=0	//Con lo que se rellena la pantalla en el caso contrario.
@CHANGE
0;JMP

(CHANGE)

@1	//Comprueba con qué rellenar la pantalla.
D=M	//D contiene negro o blanco.

@0
A=M	//Obtiene la dirección del pixel de pantalla para rellenarlo.
M=D	//lo rellena.

@0
D=M+1	//Siguiente pixel.
@KBD
D=A-D

@0
M=M+1	//Siguiente pixel.
A=M

@CHANGE
D;JGT	//Si A=0 toda la pantalla se vuelve negra.
@RESTART
0;JMP