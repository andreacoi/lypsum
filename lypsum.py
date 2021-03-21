# This is a sample Python script.

# Press Maiusc+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Importo sys per la gestione degli argomenti tramite terminale
import sys

# Importo pyperclip per la gestione della clipboard, xclip è una dipendenza necessaria
# per installare xclip su Linux - sudo apt install xclip
import pyperclip

import loremgenerator


def lypsumstart(name):
    return variable


if __name__ == '__main__':
    # eseguo il listing degli argomenti passati via terminale
    for i, arg in enumerate(sys.argv):
        # escludo l'argomento che rappresenta l'entry point del programma (lypsum.py - sys.argv[0])
        if i != 0:
            # argomento per visualizzare a schermo quanto generato
            if arg == "-p":
                print(variable)
            # argomento per generare un nuovo lorem ipsum
            elif arg == "-g":
                variable = loremgenerator.generator(sys.argv)
            # argomento per copiare il lorem ipsum nella clipboard
            elif arg == "-c":
                print("Lorem ipsum copiato nella clipboard")
                pyperclip.copy(variable)
            # argomento per visualizzare la guida utente - da costruire
            elif arg == "-h" or "--help":
                print("guida utente")
            # Avviso di argomento non valido
            else:
                print("Argomento non valido. Usa -h o --help per ricevere istruzioni sul comando lypsum.")
        # else:
        #     print("Devi dichiarare almeno un argomento. Usa -h o --help per ricevere istruzioni sul comando lypsum.")