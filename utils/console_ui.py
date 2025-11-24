# Gestion de l'affichage dans la console (menus, couleurs, messages)

from utils.colors import Colors

class ConsoleUI:

    @staticmethod
    def color_text(text, color):
        return f"{color}{text}{Colors.RESET}"

    @staticmethod
    def info(text):
        print(ConsoleUI.color_text(text, Colors.BLUE))

    @staticmethod
    def success(text):
        print(ConsoleUI.color_text(text, Colors.GREEN))

    @staticmethod
    def warning(text):
        print(ConsoleUI.color_text(text, Colors.YELLOW))

    @staticmethod
    def error(text):
        print(ConsoleUI.color_text(text, Colors.RED))

    @staticmethod
    def title(text):
        print(ConsoleUI.color_text(f"\n=== {text} ===", Colors.MAGENTA))

    @staticmethod
    def prompt(text):
        return input(ConsoleUI.color_text(text, Colors.CYAN))

    @staticmethod
    def separator():
        print(ConsoleUI.color_text("-" * 40, Colors.BRIGHT_BLACK))
