# This is a sample Python script.

# Press Maiusc+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Importo sys per la gestione degli argomenti tramite terminale
import sys

# Importo pyperclip per la gestione della clipboard, xclip è una dipendenza necessaria
import pyperclip

import loremgenerator


def print_hi(name):
    print(f'Hi, {name}')


if __name__ == '__main__':
    for i, arg in enumerate(sys.argv):
        if i != 0:
            if arg == "-p":
                print("print")
            elif arg == "-c":
                print("copia nella clipboard")
            elif arg == "-g":
                print("generate")
            elif arg == "-h" or "--help":
                print("guida utente")
            else:
                print("Argomento non valido. Usa -h o --help per ricevere istruzioni sul comando lypsum.")