# This is a sample Python script.

# Press Maiusc+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Importo sys per la gestione degli argomenti tramite terminale
import argparse
import sys

# Importo pyperclip per la gestione della clipboard, xclip è una dipendenza necessaria
# per installare xclip su Linux - sudo apt install xclip
import pyperclip

import loremgenerator


def lypsumstart(name):
    variable = "ciao"
    return variable


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--help', default='gino', type=str, help='ginoginogino')
    parser.add_argument('--arg2', default='ginopippo', type=str, help='test arg2')
    args = parser.parse_args()
