##### Pseudo code #####

# Vraag eerst de prijs van het gekozen product en de hoeveelheid van de inworp.
# input de prijs van het product
# input de hoeveelheid van de inworp

# Controleer of er wisselgeld uitgeworpen moet worden of dat er meer geld ingeworpen moet worden.
# if prijs groter dan inworp
#   zeg resterend bedrag is prijs - inworp
# elif prijs kleiner dan inworp
#   zeg u krijgt het volgende wisselgeld
#   x // 50 om aantal van een munt te berekenen
#   x = x % 50 om x het resterende aantal te maken
#   x // 20
#   x = x % 20
#   etc...
#   of een for loop, for m in munten ([50, 20, 10, 5, 2, 1])
# else
#   zeg genoeg betaald

# Echte code

# Vraag eerst de prijs van het gekozen product en de hoeveelheid
# van de inworp.
prijs = int(input('De prijs van het gekozen product is: '))
inworp = int(input('Het betaalde bedrag: '))


# Print hoe vaak iedere munt in wisselgeld past, en verandert wisselgeld vervolgens
# tot het resterende bedrag. Dit voor iedere munt.
def bereken_wisselgeld(wisselgeld, munten):
    for m in munten:
        print('Het aantal munten van', m, 'eurocent is', str(wisselgeld // m))
        if m != munten[-1]:
            wisselgeld = wisselgeld % m


# Controleer of er wisselgeld uitgeworpen moet worden of dat er
# meer geld ingeworpen moet worden.
if prijs > inworp:
    print('U moet nog', prijs - inworp, 'cent inwerpen.')
elif prijs < inworp:
    print('U krijgt', inworp - prijs, 'cent terug.')
    bereken_wisselgeld(inworp - prijs, [50, 20, 10, 5, 2, 1])
else:
    print('U heeft genoeg betaald.')

