import datetime
import locale


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