# !/usr/bin/env python
# ------------------------------------------------------
# Dateiname: main.py
# Aufgabe: Sortieren einer Textdatei
#
# Python v1.1
# Autor: xqi
# Datum: 10.04.2025
# -----------------------------------------------------

import shutil
import sys
import os
from random import randint
import colorama


# Initialize colorama
colorama.init()

# ----------------------------------------------------------------------------------------------------------------------
# TERMINAL UI CLASS
# ----------------------------------------------------------------------------------------------------------------------
class UI:
    def __init__(self):
        self.banner = r'''
                                       ______
                    |\_______________ (_____\\______________
            HH======#H###############H#######################  
                    ' ~""""""""""""""`##(_))#H\"""""Y########    
                                      ))    \#H\       `"Y###
                                      "      }#H)
        '''
        self.colors = {
            "reset": colorama.Fore.RESET,
            "main": colorama.Fore.LIGHTCYAN_EX,
            "maindark": colorama.Fore.CYAN,
            "accent": colorama.Fore.MAGENTA,
            "success": colorama.Fore.LIGHTGREEN_EX,
            "error": colorama.Fore.LIGHTRED_EX,
            "warning": colorama.Fore.LIGHTYELLOW_EX
        }

        # Borders with accent color
        self.top_border = f"{self.colors['accent']}┌─────────────────────────────────────────────────────────────────────────────────────┐{self.colors['reset']}"
        self.bottom_border = f"{self.colors['accent']}└─────────────────────────────────────────────────────────────────────────────────────┘{self.colors['reset']}"

    def clear(self):
        """Clears the console screen."""
        os.system("cls" if os.name == "nt" else "clear")

    def print_banner(self):
        """Prints the main banner with colors"""
        self.clear()
        print(f"{self.colors['main']}{self.banner}{self.colors['reset']}")

    def print_centered(self, text, color="main"):
        """Prints centered text with specified color"""
        terminal_width = shutil.get_terminal_size().columns
        print(f"{self.colors[color]}{text.center(terminal_width)}{self.colors['reset']}")

    def input_prompt(self, prompt):
        """Displays a colored input prompt"""
        return input(f"{self.colors['accent']}[?] {prompt}{self.colors['reset']} > ")

    def menu_option(self, key, text):
        """Displays a menu option with colored formatting"""
        print(f" {self.colors['accent']}{key}{self.colors['reset']} > {self.colors['main']}{text}")

    def message(self, msg_type, text):
        """Displays a colored message (success, error, warning, etc.)"""
        print(f"{self.colors[msg_type]}[{msg_type[0].upper()}] {text}{self.colors['reset']}")

    def display_menu(self):
        """Displays the main menu"""
        self.print_banner()
        self.print_centered(self.top_border)
        self.menu_option("0", "Exit")
        self.menu_option("1", "TASK 1")
        self.menu_option("2", "TASK 2")
        self.menu_option("v1.1", "TASK v1.1")
        self.print_centered(self.bottom_border)

    def task_header(self):
        """Displays the task header format"""
        self.print_banner()
        self.print_centered(self.top_border)


# ----------------------------------------------------------------------------------------------------------------------
# SUBPROGRAMS
# ----------------------------------------------------------------------------------------------------------------------
def aufgabe_1(ui):
    """Task 1: Reads and processes numbers from a file"""
    ui.task_header()

    path = "./"
    filename = "output.txt"
    output_filename = "processed_output.txt"

    try:
        os.makedirs(path, exist_ok=True)

        # Create file with random numbers
        with open(os.path.join(path, filename), "w", encoding="utf-8") as file:
            for _ in range(10):
                file.write(f"{randint(1, 100)}\n")

        # Read and process numbers
        with open(os.path.join(path, filename), "r", encoding="utf-8") as file:
            numbers = [int(line.strip()) for line in file.readlines()]

        numbers.sort()
        average = sum(numbers) / len(numbers) if numbers else 0
        maximum = max(numbers) if numbers else None

        # Save results
        with open(os.path.join(path, output_filename), "w", encoding="utf-8") as out_file:
            out_file.write("Sortierte Zahlen:\n")
            for num in numbers:
                out_file.write(f"{num}\n")
            out_file.write(f"\nDurchschnittliche Zahl: {average}\n")
            out_file.write(f"Maximale Zahl: {maximum}\n")

        # Display results
        output = " | ".join([f"{numbers[i]}" for i in range(len(numbers))])
        ui.print_centered(output)
        ui.print_centered(f"Durchschnitt: {average} | Maximum: {maximum}")
        ui.message("success", "Task completed successfully")

    except Exception as e:
        ui.message("error", f"Fehler beim Verarbeiten der Datei: {e}")

    ui.print_centered(ui.bottom_border)
    ui.input_prompt("Press Enter to return to menu")


def aufgabe_2(ui):
    """Task 2: Placeholder function"""
    ui.task_header()
    ui.print_centered("Task 2 functionality not yet implemented")
    ui.print_centered(ui.bottom_border)
    ui.input_prompt("Press Enter to return to menu")


def aufgabe_3(ui):
    """Task v1.1: Placeholder function"""
    ui.task_header()
    ui.print_centered("Task v1.1 functionality not yet implemented")
    ui.print_centered(ui.bottom_border)
    ui.input_prompt("Press Enter to return to menu")


# ----------------------------------------------------------------------------------------------------------------------
# MAIN PROGRAM
# ----------------------------------------------------------------------------------------------------------------------
def main():
    ui = UI()

    while True:
        ui.display_menu()
        command = ui.input_prompt("MENU")

        match command:
            case "0":
                sys.exit()
            case "1":
                aufgabe_1(ui)
            case "2":
                aufgabe_2(ui)
            case "v1.1":
                aufgabe_3(ui)
            case _:
                ui.task_header()
                ui.message("error", "Ungültige Eingabe! Bitte erneut versuchen.")
                ui.print_centered(ui.bottom_border)
                ui.input_prompt("Press Enter to return to menu")


if __name__ == "__main__":
    main()
