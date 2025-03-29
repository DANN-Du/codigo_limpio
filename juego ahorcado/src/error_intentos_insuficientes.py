class ErrorIntentosInsuficientes(Exception):
    """
        Excepción personalizada que se lanza cuando el jugador ha agotado todas sus oportunidades
        para adivinar la palabra en el juego de adivinanza.
    """

    def __init__(self):
        """
            Inicializa la excepción con un mensaje predeterminado indicando que los intentos se han agotado.
        """
        super().__init__(f"se han agotado las oportunidades para adivinar la palabra")
