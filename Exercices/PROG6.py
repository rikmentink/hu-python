import datetime
import locale


# ----- 6.1 ----- #
def convert(temp):
    return (temp * 1.8) + 32


def table():
    table = '{:^6}{:^12}'.format('F', 'C')
    for temp in range(-30, 50):
        if temp % 10 == 0:
            table = table + '\n{:^6}{:>8.1f}'.format(convert(temp), temp)

    return table


# ----- 6.2 ----- #
def pretty_print():
    output = ''
    with open('Bestanden/kaartnummers.txt', 'r') as file:
        lines = file.read().splitlines()
        for line in lines:
            data = line.split(', ')
            output = output + data[1] + f' heeft kaartnummer: {data[0]}\n'
    return output


# ----- 6.3 ----- #
def analyse():
    with open('Bestanden/kaartnummers.txt', 'r') as file:
        kaarten = []

        for kaart in file.read().splitlines():
            kaarten.append(kaart.split(', '))

        kaarten.sort()

        return f'Dit bestand telt {len(kaarten)} regels\nHet grootste kaartnummer is: {kaarten[-1][0]} en dat staat op regel {kaarten.index(kaarten[-1])}'


# ----- 6.4 ----- #
def registratie():
    file = open('Bestanden/hardlopers.txt', 'a')

    print('Voer achtereenvolgend namen van de hardlopers in. Voer "stop" in om het programma te stoppen.')
    while True:
        hardloper = input('Hardloper: ')

        if len(hardloper.strip()) == 0:
            print('Voer een naam in of voer "stop" in om te stoppen.')
            continue

        if hardloper == 'stop':
            print('Het programma wordt gestopt.')
            file.close()
            break

        locale.setlocale(locale.LC_TIME, 'nl_NL')
        datum = datetime.datetime.now().strftime('%A %d %B %Y, %H:%M:%S').capitalize()

        file.write(f'{datum};{hardloper}\n')
        continue


# ----- 6.5 ----- #
def gemiddelde():
    text = input('Voer een willekeurige zin in:\n')
    woorden = text.split(' ')

    lengtes = [len(woord) for woord in woorden]
    gemiddeld = 0 if len(lengtes) == 0 else (sum(lengtes) / len(lengtes))

    return f'De gemiddelde lengte is {round(gemiddeld, 2)} tekens.'