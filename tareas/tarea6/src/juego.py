'''
NAME
    juego.py
  
VERSION
    1.0

AUTHOR
    Valentina Janet Arias Ojeda

DESCRIPTION
    Juego de piedra, papel y tijera

CATEGORY
   Game  

ARGUMENTS
    None    


'''
# Importamos librería necesaria para que la computadora reciba valores al azar.
import random
# Función que permite que la computadora tenga una decisión aleatoria.
def obtener_opcion_computadora():
    habilidades = ["piedra", "papel", "tijera"]
    return random.choice(habilidades)
# Función que determina quién gana.
def determinar_ganador(player_choice, npc_choice):
    # Cambiar el input del usuario a minúsculas para que no haya errores con mayúsculas y minúsculas
    player_choice = player_choice.lower()
    npc_choice = npc_choice.lower()
    # Reglas del juego
    if player_choice == npc_choice:
        return "empate"
    elif (player_choice == "piedra" and npc_choice == "tijera") or \
         (player_choice == "papel" and npc_choice == "piedra") or \
         (player_choice == "tijera" and npc_choice == "papel"):
        return "player"
    else:
        return "npc"
# Main
print("Este es el juego de piedra, papel o tijera.")
# Preguntar el nombre del usuario
player = input("¿Cómo te llamas?: ")
# Solicitar al usuario su decisión
print(f"Ok, {player}, teclea tu opción (Recuerda que puedes elegir piedra, papel o tijera):")
player_choice = input()
# Llamada a función para obtener decisión de la computadora
npc_choice = obtener_opcion_computadora()
# Imprimir las decisiones de ambos 
print(f"\n{player_choice}: {player_choice}")
print(f"Computadora: {npc_choice}\n")
# Llamada a función que determina el ganador
winner = determinar_ganador(player_choice, npc_choice)
# Impresión de resultado final
if winner == "player":
    print(f"Felicidades {player}, me ganaste!")
elif winner == "npc":
    print("Perdiste!")
else:
    print("Es un empate!!!!")
