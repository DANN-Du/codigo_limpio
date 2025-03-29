from src.diccionario import Diccionario
from src.adivinanza import Adivinanza
from src.error_intentos_insuficientes import ErrorIntentosInsuficientes


class Juego:
    """
    Clase que representa un juego de adivinanza de palabras. 
    Permite configurar la dificultad, gestionar intentos y verificar el progreso del jugador.
    """
    DIFICULTAD_BAJA = "DIFICULTAD_BAJA"
    DIFICULTAD_MEDIA = "DIFICULTAD_MEDIA"
    DIFICULTAD_ALTA = "DIFICULTAD_ALTA"

    def __init__(self):
        """
        Inicializa el juego con dificultad baja por defecto y sin una palabra generada.
        """
        self.__dificultad = Juego.DIFICULTAD_BAJA
        self.__intentos_realizados: int = 0
        self.__diccionario = Diccionario()
        self.__adivinanza: Adivinanza = None

    def obtener_intentos_realizados(self) -> int:
        """
        Obtiene la cantidad de intentos realizados hasta el momento.

        Returns:
            int: Número de intentos realizados..
        """
        return self.__intentos_realizados

    def obtener_adivinanza(self) -> Adivinanza:
        """
        Obtiene el objeto Adivinanza asociado a la partida en curso.

        Returns:
            Adivinanza: Objeto que representa la adivinanza actual.
        """
        return self.__adivinanza

    def __generar_palabra(self) -> str:
        """
        Genera una palabra aleatoria del diccionario.

        Returns:
            str: Palabra seleccionada aleatoriamente.
        """
        return self.__diccionario.obtener_palabra()

    def calcular_intentos_permitidos(self) -> int:
        """
        Calcula la cantidad de intentos permitidos según la dificultad establecida.

        Returns:
            int: Número de intentos permitidos según la dificultad del juego.
        """
        if self.__dificultad == self.DIFICULTAD_BAJA:
            return 20
        if self.__dificultad == self.DIFICULTAD_MEDIA:
            return 10
        if self.__dificultad == self.DIFICULTAD_ALTA:
            return 5
        return 0

    def modificar_dificultad(self, dificultad: str) -> None:
        """
        Modifica la dificultad del juego.

        Args:
            dificultad (str): Nivel de dificultad a establecer (baja, media o alta).
        """
        self.__dificultad = dificultad

    def iniciar_partida(self) -> int:
        """
        Inicia una nueva partida generando una palabra y estableciendo los intentos disponibles.

        Returns:
            int: Cantidad de letras en la palabra generada.
        """
        palabra = self.__generar_palabra()
        self.__adivinanza: Adivinanza = Adivinanza(palabra)
        self.__intentos_realizados = self.calcular_intentos_permitidos()
        return self.__adivinanza.obtener_cantidad_posiciones()

    def adivinar(self, letra: str) -> [int]:
        """
        Intenta adivinar una letra de la palabra.

        Args:
            letra (str): Letra que el jugador quiere adivinar.

        Returns:
            list[int]: Lista con las posiciones donde aparece la letra en la palabra. Vacía si la letra no está.

        Raises:
            ErrorIntentosInsuficientes: Si no quedan intentos disponibles.
        """
        if self.__intentos_realizados < 0:
            raise ErrorIntentosInsuficientes()
        self.__intentos_realizados -= 1
        return self.__adivinanza.adivinar(letra)

    def verificar_si_hay_intentos(self) -> bool:
        """
        Verifica si quedan intentos disponibles para adivinar.

        Returns:
            bool: True si aún hay intentos disponibles, False en caso contrario.
        """
        return self.__intentos_realizados >= 0

    def verificar_triunfo(self) -> bool:
        """
        Verifica si el jugador ha adivinado completamente la palabra.

        Returns:
            bool: True si la palabra ha sido adivinada, False en caso contrario.
        """
        return self.__adivinanza.verificar_si_hay_triunfo()