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
    parser = argparse.ArgumentParser(description='Lorem ipsum CLI generator.', add_help=False)
    parser.add_argument('--paragraph', '-p', default='5', type=int, help='Set the number of paragraph to generate')
    parser.add_argument('--single', '-s', action='store_false', default=argparse.SUPPRESS, help='Generate a single pseudorandom phrase')
    parser.add_argument('--words', '-w', default='8', type=int, help='Set the number of words to generate')
    parser.add_argument('-v', '--verbose', action='store_false', default=argparse.SUPPRESS, help='Verbose mode')
    parser.add_argument('-h', '--help', action='help', default=argparse.SUPPRESS, help='Show this help message and exit.')
    args = parser.parse_args()
