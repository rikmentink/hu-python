import json
import locale
from datetime import datetime as dt
from os import path


# ----- 10.1 ----- #
def stationslijst():
    # Lees JSON bestand
    # Print van alle stations de lange naam, code en het type
    # Print het meest oostelijk gelegen station
    with open('Bestanden/stations.json', 'r') as file:
        stations = json.load(file)['payload']

    print('Dit zijn de namen, codes en types van elk station:')

    meest_oostelijk = []

    for station in stations:
        naam = station['namen']['lang']
        code = station['code']
        type = station['stationType']

        print('{:25} - {:6} : {}'.format(naam, code, type))
        if meest_oostelijk == [] or station['lng'] > meest_oostelijk['lng']:
            meest_oostelijk = station

    print(f'\nHet meest oostelijk gelegen station is: {meest_oostelijk["namen"]["lang"]}')

# stationslijst()


# ----- 10.2 ----- #
def inloggen():
    bestand = 'Bestanden/pe_10_2_inloggers.json'

    while True:
        print('Vul de volgende gegevens in om in te loggen:')
        """
        Vraag om alle gegevens d.m.v. inputs.
        """
        naam = input("Wat is je achternaam? ")
        if naam.lower().strip() == 'einde':
            print('Programma wordt gestopt. Tot ziens!')
            break

        voorl = input("Wat zijn je voorletters? ")
        gbdatum = input("Wat is je geboortedatum? ")
        email = input("Wat is je e-mailadres? ")

        """
        Haal de huidige datum op, met de juiste formatting.
        """
        locale.setlocale(locale.LC_TIME, 'nl_NL')
        datum = dt.now().strftime('%A %d %B %Y, %H:%M:%S').capitalize()

        """
        Creëer een dictionary met de gegevens van deze login.
        """
        persoon = {
            'login_datum': datum,
            'naam': naam,
            'voorletters': voorl,
            'geb_datum': gbdatum,
            'e-mail': email,
        }

        """
        Schrijf de login naar het json-bestand.
        """
        with open(bestand, 'w+') as file:
            personen = []

            if path.getsize(bestand) != 0:
                personen = json.load(file)

            personen.append(persoon)
            file.seek(0)
            json.dump(personen, file)

        print('Bedankt!\n')