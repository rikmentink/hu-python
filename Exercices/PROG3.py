# ----- 3.1 ----- #
cijferPROJA = 7
cijferPROG  = 8
cijferMOD   = 6.5

gemiddelde = (cijferPROJA + cijferPROG + cijferMOD) / 3
beloning   = (gemiddelde * 30) * 3
overzicht  = 'Mijn cijfers (gemiddeld een ' + str(round(gemiddelde, 1)) + ') leveren een beloning van € ' + str(beloning) + ' op!'

print(overzicht)


# ----- 3.2 ----- #
print(0 == (1 == 2))
print((2 + (3 == 4) + 5) == 7)
print((1 < -1) == (3 > 4))


# ----- 3.3 ----- #
uurloon = input('Wat verdien je per uur: ')
aantalUur = input('Hoeveel uur heb je gewerkt: ')

print(str(aantalUur) + ' uur werken levert €' + str(int(aantalUur) * int(uurloon)) + ' op')
