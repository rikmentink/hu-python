### 4.1 ###
score = int(input('Geef je score: '))

if score > 15:
    print('Gefeliciteerd!')
    print('Met een score van', score, 'ben je geslaagd!')
else:
    print('Helaas!')
    print('Met een score van', score, 'ben je niet geslaagd.')

### 4.2 ###
age = int(input('Geef je leeftijd: '))
passport = input('Nederlands paspoort: ')

if age >= 18 and passport == 'Ja' or 'ja':
    print('Gefeliciteerd, je mag stemmen.')
else:
    print('Je mag helaas niet stemmen.')

# TODO: 4.3 t/m 4.5

### 4.6 ###
s = "Guido van Rossum heeft programmeertaal Python bedacht."
klinkers = ['a', 'o', 'u', 'i', 'e']

for letter in s:
    if letter in klinkers:
        print(letter)