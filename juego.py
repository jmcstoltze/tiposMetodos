from personaje import (
    Personaje,
)  # Importa la clase Personaje desde el archivo personaje.py
import random  # Importa el módulo random para generar números aleatorios

# Imprime un mensaje de bienvenida al juego
print("¡Bienvenido a Gran Fantasía!")
# Solicita al usuario ingresar el nombre de su personaje y lo almacena en la variable nombre
nombre = input("Por favor indique nombre de su personaje:\n")

# Crea una instancia de la clase Personaje con el nombre proporcionado por el usuario
p = Personaje(nombre)
# Imprime el estado actual del personaje
print(p.estado)

# Imprime un mensaje indicando que ha aparecido un orco
print("\n¡Oh no!, ¡Ha aparecido un Orco!")
# Crea una instancia de la clase Personaje para representar al orco
o = Personaje("Orco")
# Calcula la probabilidad de ganar la batalla contra el orco
probabilidad_ganar = p.get_probabilidad_ganar(o)

# Muestra un diálogo con opciones para el jugador y almacena la opción elegida por el jugador en la variable opcion_orco
opcion_orco = Personaje.mostrar_dialogo_opcion(probabilidad_ganar)

# Si la opción elegida por el jugador es atacar:
while opcion_orco == 1:
    # Genera aleatoriamente un resultado ("G" para ganar, "P" para perder) basado en la probabilidad de ganar
    resultado = "G" if random.uniform < probabilidad_ganar else "P"

    # Si el resultado es ganar:
    if resultado == "G":
        # Imprime un mensaje de victoria y la cantidad de experiencia ganada
        print(
            "\n¡Le has ganado al orco, felicidades!\n"
            "¡Recibirás 50 puntos de experiencia!\n"
        )
        # Incrementa la experiencia del personaje en 50 puntos
        p.estado = 50
        # Reduce la experiencia del orco en 30 puntos
        o.estado = -30

    # Si el resultado es perder:
    else:
        # Imprime un mensaje de derrota y la cantidad de experiencia perdida
        print(
            "\n¡Oh no! ¡El orco te ha ganado!\n"
            "¡Has perdido 30 puntos de experiencia!\n"
        )
        # Reduce la experiencia del personaje en 30 puntos
        p.estado = -30
        # Incrementa la experiencia del orco en 50 puntos
        o.estado = 50

    # Imprime el estado actual del personaje
    print(p.estado)
    # Imprime el estado actual del orco
    print(o.estado)

    # Calcula la nueva probabilidad de ganar la batalla contra el orco
    probabilidad_ganar = p.get_probabilidad_ganar(o)
    # Muestra un diálogo con opciones para el jugador y almacena la opción elegida por el jugador en la variable opcion_orco
    opcion_orco = Personaje.mostrar_dialogo_opcion(probabilidad_ganar)
