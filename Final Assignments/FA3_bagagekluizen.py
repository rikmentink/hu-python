import builtins
import collections
import json
import random
import sys
import traceback

"""
Programming
Final assignment 3: Bagagekluizen
(c) 2021 Hogeschool Utrecht,
Tijmen Muller en 
Bart van Eijkelenburg (bart.vaneijkelenburg@hu.nl)


Opdracht:
Werk onderstaande functies uit.
Voeg commentaar toe om je code toe te lichten.
Lever je werk in op Canvas als alle tests slagen.
"""


def aantal_kluizen_vrij():
    """
    Bepaal hoeveel kluizen er nog vrij zijn. Er zijn in totaal 12 kluizen,
    dus 12 min het aantal kluizen dat in het bestand staat, moet de uitkomst
    van deze functie zijn.

    Returns:
        int: Het aantal vrije kluizen.
    """
    with open('kluizen.txt', 'r') as file:
        return 12 - len(file.readlines())


def nieuwe_kluis():
    """
    Indien er nog kluizen vrij zijn, moet de gebruiker de mogelijkheid krijgen
    om een kluiscode in te voeren. Deze kluiscode moet uit minimaal 4 tekens bestaan,
    en de puntkomma (';') mag er niet in voorkomen.

    Als de puntkomma voorkomt in de kluiscode, is de returnwaarde van deze functie -1.
    Als er geen vrije kluizen meer zijn, is de returnwaarde van deze functie -2.

    Als er nog vrij kluizen zijn, en de kluiscode is geldig, dan koppelt deze functie
    de kluiscode aan een nog beschikbare kluis, en schrijft deze combinatie weg naar
    een tekstbestand. De returnwaarde van de functie is dan gelijk aan het toegekende
    kluisnummer.

    Returns:
        int: het toegekende kluisnummer of foutcode -1 of -2
    """
    if aantal_kluizen_vrij() == 0:
        return -2

    # Kluiscode invoeren
    while True:
        code = input('Voer een code in:\n')
        if len(code) < 4:
            print('Code is te kort.\n')
            continue
        if ';' in code:
            return -1
        break


    # Koppel random kluisnummer
    with open('kluizen.txt') as file:
        bezette_kluizen = []
        for kluis in file.readlines():
            bezette_kluizen.append(int(kluis.split(';')[0]))

        for nummer in range(1, 13):
            if str(nummer) not in bezette_kluizen:
                kluisnummer = nummer

    # Schrijf naar bestand
    with open('kluizen.txt', 'a') as file:
        file.write(f'{kluisnummer};{code}\n')

    return kluisnummer

def kluis_openen():
    """
    Laat de gebruiker een kluisnummer invoeren, en direct daarna de bijbehorende
    kluiscode. Indien deze combinatie voorkomt in het tekstbestand met de kluizen
    die in gebruik zijn, is het resultaat van de functie True, anders False.

    Returns:
        bool: True als de ingevoerde combinatie correct is, anders False
    """
    kluisnummer = input('Voer uw kluisnummer in:\n')
    code = input('Voer uw code in:\n')

    with open('kluizen.txt', 'r') as file:
        kluizen = file.readlines()
        for kluis in kluizen:
            kluis = kluis.split(';')
            kluis[1] = kluis[1].replace('\n', '')

            if kluisnummer == kluis[0] and code == kluis[1]:
                return True
            else:
                return False


def kluis_teruggeven():
    """
    Laat de gebruiker een kluisnummer invoeren, en direct daarna de bijbehorende
    kluiscode. Indien deze combinatie voorkomt in het tekstbestand met de kluizen
    die in gebruik zijn, moet deze combinatie/regel uit het tekstbestand verwijderd
    worden.

    Als het lukt om de combinatie te vinden en te verwijderen, is het resultaat
    van de functie True, anders False.

    Returns:
        bool: True als er een kluiscombinatie verwijderd werd, anders False
    """
    while True:
        kluisnummer = input('Voer uw kluisnummer in:\n')

        if int(kluisnummer) not in range(1, 13):
            print('Voer een geldig kluisnummer.\n')
            continue
        break
    code = input('Voer uw code in:\n')

    nieuwe_lijst = []

    with open('kluizen.txt', 'r') as file:
        kluizen = file.readlines()
        if not kluizen:
            return False

        for kluis in kluizen:
            huidige_kluis = kluis.split(';')
            if huidige_kluis[0] != str(kluisnummer) or huidige_kluis[1].replace('\n', '') != code:
                nieuwe_lijst.append(kluis)

    with open('kluizen.txt', 'w') as file:
        file.writelines(nieuwe_lijst)

    return True