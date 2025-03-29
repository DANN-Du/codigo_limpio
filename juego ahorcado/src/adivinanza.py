class Adivinanza:
    """
    Representa una palabra a adivinar en el juego del ahorcado.

    Attributes:
        __letras (list[str]): Lista de caracteres que conforman la palabra a adivinar.
        __posiciones (list[bool]): Lista de booleanos que indican si cada letra ha sido adivinada.
    """

    def __init__(self, palabra: str):
        """
        Inicializa una nueva instancia de Adivinanza con la palabra dada.

        Args:
            palabra (str): La palabra que debe adivinarse.
        """
        self.__letras: list[str] = list(palabra)
        self.__posiciones: list[bool] = [False] * len(self.__letras)

    def adivinar(self, letra: str) -> list[int]:
        """
        Intenta adivinar una letra en la palabra.

        Args:
            letra (str): La letra a adivinar.

        Returns:
            list[int]: Lista con las posiciones donde se encuentra la letra en la palabra.
                        Si la letra no está presente, devuelve una lista vacía.
        """
        if letra not in self.__letras:
            return []

        posiciones_donde_esta_la_letra = []
        for i in range(len(self.__letras)):
            if self.__letras[i] == letra:
                posiciones_donde_esta_la_letra.append(i)
                self.__posiciones[i] = True
        return posiciones_donde_esta_la_letra

    def obtener_letras(self) -> list[str]:
        """
        Obtiene la lista de letras de la palabra a adivinar.

        Returns:
            list[str]: Lista de caracteres que conforman la palabra.
        """
        return self.__letras

    def obtener_posiciones(self) -> list[bool]:
        """
        Obtiene la lista de posiciones adivinadas.

        Returns:
            list[bool]: Lista de booleanos que indican qué letras han sido adivinadas.
        """
        return self.__posiciones

    def obtener_cantidad_posiciones(self) -> int:
        """
        Obtiene la cantidad total de letras en la palabra a adivinar.

        Returns:
            int: Número total de letras en la palabra.
        """
        return len(self.__letras)

    def verificar_si_hay_triunfo(self) -> bool:
        """
        Verifica si todas las letras han sido adivinadas.

        Returns:
            bool: True si todas las letras han sido adivinadas, False en caso contrario.
        """
        return all(self.__posiciones)
