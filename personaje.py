class Personaje:
    def __init__(self, nombre):
        """
        Constructor de la clase Personaje.

        Parámetros:
        nombre (str): El nombre del personaje.
        """
        self.nombre = nombre
        self.nivel = 1  # Nivel inicial del personaje
        self.experiencia = 0  # Experiencia inicial del personaje

    @property
    def estado(self):
        """
        Método de solo lectura que devuelve el estado actual del personaje.

        Retorna:
        tuple: Una tupla con información sobre el nombre, nivel y experiencia del personaje.
        """
        return (
            f"Nombre: {self.nombre}",
            f"Nivel {self.nivel}",
            f"Experiencia: {self.experiencia}",
        )

    @estado.setter
    def estado(self, exp: int):
        """
        Setter para actualizar el estado del personaje después de una acción.

        Parámetros:
        exp (int): La cantidad de experiencia ganada o perdida por el personaje.
        """
        tmp_exp = self.experiencia + exp

        # Actualizar el nivel basado en la experiencia acumulada
        while tmp_exp >= 100:
            self.nivel += 1
            tmp_exp -= 100

        # Ajustar la experiencia si es negativa y el nivel no es 1
        while tmp_exp < 0:
            if self.nivel > 1:
                tmp_exp = 100 + tmp_exp
                self.nivel -= 1
            else:
                tmp_exp = 0

        self.experiencia = tmp_exp

    def __lt__(self, other):
        """
        Método mágico para comparar el nivel de este personaje con otro personaje.

        Retorna:
        bool: True si el nivel de este personaje es menor que el nivel del otro personaje, False en caso contrario.
        """
        return self.nivel < other.nivel

    def __gt__(self, other):
        """
        Método mágico para comparar el nivel de este personaje con otro personaje.

        Retorna:
        bool: True si el nivel de este personaje es mayor que el nivel del otro personaje, False en caso contrario.
        """
        return self.nivel > other.nivel

    def __eq__(self, other):
        """
        Método mágico para comparar el nivel de este personaje con otro personaje.

        Retorna:
        bool: True si el nivel de este personaje es igual al nivel del otro personaje, False en caso contrario.
        """
        return self.nivel == other.nivel

    def get_probabilidad_ganar(self, other):
        """
        Calcula la probabilidad de ganar en una batalla contra otro personaje.

        Parámetros:
        other (Personaje): El otro personaje contra el que se va a combatir.

        Retorna:
        float: La probabilidad de ganar la batalla.
        """
        if self < other:
            return 0.33
        elif self > other:
            return 0.66
        else:
            return 0.5

    @staticmethod
    def mostrar_dialogo_opcion(probabilidad_ganar):
        """
        Muestra un diálogo y opciones para el jugador antes de una batalla.

        Parámetros:
        probabilidad_ganar (float): La probabilidad de ganar la batalla.

        Retorna:
        int: La opción elegida por el jugador (1 para atacar, 2 para huir).
        """
        return int(
            input(
                f"\nCon tu nivel actual, tienes {probabilidad_ganar * 100}% "
                "de probabilidades de ganarle al Orco.\n"
                "\nSi ganas, ganarás 50 puntos de experiencia y el orco perderá 30. \n"
                "Si pierdes, perderás 30 puntos de experiencia y el orco ganará 50.\n"
                "\n¿Qué deseas hacer?\n"
                "1. Atacar\n"
                "2. Huir\n"
            )
        )
