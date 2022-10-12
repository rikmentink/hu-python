import random


### 9.1 ###
bruin = {'Boxtel', 'Best', 'Beukenlaan', 'Eindhoven', 'Helmond \'t hout', 'Helmond', 'Helmond Brouwhuis', 'Deurne'}
groen = {'Boxtel', 'Best', 'Beukenlaan', 'Eindhoven', 'Geldrop', 'Heeze', 'Weert'}

overeenkomst = []
for lijn in bruin, groen:
    for station in lijn:
        if station in bruin and station in groen:
            overeenkomst.append(station)
#print(set(overeenkomst))


### 9.2 ###
def monopolyworp():
    """
    Gooit 2 dobbelstenen en print het resultaat in een lijst met tupels. Als
    de 2 dobbelstenen hetzelfde zijn, print hij het resultaat en gooit hij
    opnieuw. Als er 3 keer hetzelfde gegooid wordt, stopt de loop en zegt hij
    dat je naar de gevangenis moet.

    :return: Een lijst met tupels, waar de worp in staat.
    """
    worpen = []

    while True:
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        worpen.append((dice1, dice2))

        if dice1 == dice2:
            if len(worpen) == 3:
                print(f'{dice1} + {dice2} = direct naar de gevangenis')
                break
            else:
                print(f'{dice1} + {dice2} = {dice1 + dice2}')
            continue
        else:
            print(f'{dice1} + {dice2} = {dice1 + dice2}')
            break

    return worpen

#print(monopolyworp())


### 9.3 ###
def code(invoerstring):
    