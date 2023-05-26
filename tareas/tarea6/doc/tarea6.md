# Tarea 6. Python: Piedra, papel o tijera.
## Valentina Janet Arias Ojeda
### Introducción

El juego de piedra, papel o tijera es un en el que dos jugadores eligen entre tres opciones posibles: piedra, papel o tijera. Sigue las siguientes reglas:

- Papel gana ante piedra.
- Papel pierde ante tijera.
- Piedra gana ante tijera.
- Piedra pierde ante papel.
- Tijera gana ante papel.
- Tijera pierde ante piedra.

### Metodología
Hemos creado una función para obtener la opción de la computadora, otra para determinar el ganador y así tener un código más estructurado y legible.
En el main:
1. El programa solicita al usuario su nombre.
2. El usuario ingresa su opción (piedra, papel o tijera).
3. La computadora genera aleatoriamente su opción.
4. Se determina quién es el ganador según las reglas del juego:
   - Si las opciones son iguales, se declara un empate.
   - Si no es un empate, se evalúan las combinaciones posibles para determinar al ganador.
5. Se muestra el resultado por pantalla, indicando quién ganó o si fue un empate.

### Instalación

El programa solo requiere python, te recomendamos instalar la última versión.

### Ejemplos

Caso 1. El usuario da la opción papel, y la computadora papel. Debe aparecer un resultado de empate.


```
¿Cómo te llamas?: hely
Ok, hely, teclea tu opción (Recuerda que puedes elegir piedra, papel o tijera):
papel

papel: papel
Computadora: papel

Es un empate!!!!

```

CAso 2. El usuario escoge tijera y la computadora piedra, debe aparecer que el usuario perdió.


```
Este es el juego de piedra, papel o tijera.
¿Cómo te llamas?: hely  
Ok, hely, teclea tu opción (Recuerda que puedes elegir piedra, papel o tijera):
tijera

tijera: tijera
Computadora: piedra

Perdiste!

```


