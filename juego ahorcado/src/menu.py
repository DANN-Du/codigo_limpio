import os
import colorama
from colorama import Fore, Style
from src.model.juego import Juego


class Menu:
    """
    Representa el menú principal del juego de adivinanza de palabras.

    Attributes:
        juego (Juego): Instancia del juego que gestiona la lógica de la partida.
    """

    def __init__(self, juego: Juego):
        """Metodo constructor, inicializa la instancia juego de la clase juego"""
        colorama.init(autoreset=True)  # Inicializar colorama para Windows
        self.juego: Juego = juego

    def __mostrar_opciones(self):
        """Muestra las opciones del menú principal"""
        print(Fore.CYAN + Style.BRIGHT + "🎮 MENÚ PRINCIPAL 🎮\n")
        print(Fore.YELLOW + "1️⃣  Jugar")
        print(Fore.GREEN + "2️⃣  Configuración")
        print(Fore.BLUE + "3️⃣  Salir\n")

    def __pedir_letra(self) -> list[int]:
        """Pide al usuario que ingrese una letra y devuelve una lista con el resultado de la palabra"""
        letra = input(Fore.YELLOW + "🎮 ¡Ingresa una letra!: ")
        return self.juego.adivinar(letra)

    def __modificar_configuracion(self):
        """Modifica la configuración del juego"""
        print(Fore.GREEN + "1️⃣  Dificultad Baja")
        print(Fore.GREEN + "2️⃣  Dificultad Media")
        print(Fore.GREEN + "3️⃣  Dificultad Alta")
        opcion = input(Fore.YELLOW + "🎮 ¡Selecciona la dificultad con la que deseas jugar!: ")

        if opcion == "1":
            self.juego.modificar_dificultad(Juego.DIFICULTAD_BAJA)
        elif opcion == "2":
            self.juego.modificar_dificultad(Juego.DIFICULTAD_MEDIA)
        elif opcion == "3":
            self.juego.modificar_dificultad(Juego.DIFICULTAD_ALTA)

    def __controlar_opcion_1(self):
        """Controla la opción 1 del menú principal, verifica la cantidad de intentos permitidos y devuelve el resultado de
        la jugada en la partida"""
        cantidad_posiciones = self.juego.iniciar_partida()
        display = Fore.RED + " _ " * cantidad_posiciones
        print(display)

        while True:
            if self.juego.verificar_triunfo():
                print(Fore.GREEN + "🎮 ¡Felicitaciones! ¡Has ganado!")
                break
            if not self.juego.verificar_si_hay_intentos():
                print(Fore.RED + "🎮 ¡Lo siento! ¡Has superado el máximo de intentos!")
                break

            intentos_permitidos = self.juego.calcular_intentos_permitidos()
            intentos_realizados = intentos_permitidos - self.juego.obtener_intentos_realizados()
            letra = input(Fore.YELLOW + f"🎮 ¡Ingresa una letra! ({intentos_realizados}/{intentos_permitidos}) ").upper()
            resultado_adivinanza = self.juego.adivinar(letra)
            self.__mostrar_resultado_jugada(resultado_adivinanza)

    def __mostrar_adivinanza(self):
        """muestra la adivinanza con las casillas que ya han sido ocupadas por las letras ingresadas"""
        letras = self.juego.obtener_adivinanza().obtener_letras()
        posiciones = self.juego.obtener_adivinanza().obtener_posiciones()
        display = ""
        for i in range(len(letras)):
            if posiciones[i]:
                display += Fore.GREEN + " " + letras[i] + " "
            else:
                display += Fore.RED + " _ "

        print(display)

    def __mostrar_resultado_jugada(self, resultado_adivinanza: list[int]):
        """Muestra el resultado de la jugada en la partida"""
        if len(resultado_adivinanza) == 0:
            print(Fore.YELLOW + "¡Lo siento, no has acertado! ¡Sigue intentando!")
        else:
            print(Fore.YELLOW + "¡Muy bien, has acertado! ¡Sigue así!")
        self.__mostrar_adivinanza()

    def iniciar(self):
        """Inicia el juego de adivinanza de palabras"""
        while True:
            self.__mostrar_opciones()
            opcion = input(Fore.MAGENTA + "👉 Selecciona una opción: ")

            if opcion == "1":
                print(Fore.YELLOW + "🎮 ¡Comenzando el juego!")
                self.__controlar_opcion_1()
            elif opcion == "2":
                print(Fore.GREEN + "⚙️  Abriendo configuración...")
                self.__modificar_configuracion()
            elif opcion == "3":
                exit()
            else:
                print(Fore.RED + "❌ Opción no válida, intenta de nuevo.")
