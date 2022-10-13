# ----- 7.1 ----- #
def seizoen(maand):
    """
    Geeft het seizoen dat bij de huidige maand hoort.

    :param maand: de maand van het jaar (1-12)
    :return: Het bijbehorende seizoen van deze maand.
    """
    if maand >= 3 and maand <= 5:
        return 'Lente'
    elif maand >= 6 and maand <= 8:
        return 'Zomer'
    elif maand >= 9 and maand <= 11:
        return 'Herfst'
    if maand == 12 or (maand >= 1 and maand <= 2):
        return 'Winter'
    else:
        return 'Ongeldig'


# ----- 7.2 ----- #
def analyzer(lijst):
    """
    Het neemt een reeks getallen gescheiden door streepjes, sorteert ze en
    retourneert een tupel van de gesorteerde lijst, het grootste getal, het
    kleinste getal, het aantal getallen, de som van de getallen en het
    gemiddelde van de getallen.

    :param lijst: een reeks getallen gescheiden door een streepje.
    :return: Een tuple met de verschillende uitgerekende waarden.
    """
    gesorteerde_lijst = [int(nummer) for nummer in lijst.split("-")]
    gesorteerde_lijst.sort()

    grootste_waarde = max(gesorteerde_lijst)
    kleinste_waarde = min(gesorteerde_lijst)
    aantal_getallen = len(gesorteerde_lijst)
    som_getallen = sum(gesorteerde_lijst)
    gemiddelde = som_getallen / aantal_getallen

    return gesorteerde_lijst, grootste_waarde, kleinste_waarde, aantal_getallen, som_getallen, gemiddelde


"""
    lijst = analyzer("5-9-7-1-7-8-3-2-4-8-7-9")
    print(f'Gesorteerde list van ints: {lijst[0]}')
    print(f'Grootste getal: {lijst[1]} en kleinste getal: {lijst[2]}')
    print(f'Aantal getallen: {lijst[3]} en som van de getallen: {lijst[4]}')
    print(f'Gemiddelde: {lijst[5]}')
"""


# ----- 7.3 ----- #
def gemiddelde_per_student(studentencijfers):
    """
    Berekent voor ieder item in de lijst het gemiddelde van die lijst.

    :param studentencijfers: een lijst met lijsten, waarvan iedere sublijst een
           cijferlijst van een student bevat.
    :return: Het gemiddelde per student.
    """
    gemiddelde = []
    for student in studentencijfers:
        gemiddelde.append(sum(student) / len(student))
    return gemiddelde


# ----- 7.4 ----- #
def gemiddelde_van_alle_studenten(studentencijfers):
    """
    Berekent het gemiddelde van de gemiddelden van iedere sublijst

    :param studentencijfers: een lijst met cijferlijsten
    :return: Het gemiddelde van alle gemiddelden van studenten.
    """
    gemiddelde = 0
    for student in studentencijfers:
        for cijfer in student:
            gemiddelde = gemiddelde + cijfer
    return gemiddelde


studentencijfers = [[95, 92, 86], [66, 75, 54], [89, 72, 100], [34, 0, 0]]
print(gemiddelde_per_student(studentencijfers))
print(gemiddelde_van_alle_studenten(studentencijfers))


# ----- 7.4 ----- #
for tafel in range(1, 11):
    for nummer in range(1, 11):
        print(f'{nummer} x {tafel} = {nummer*tafel}')