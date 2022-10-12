### 8.1 ###
"""
getallen = []
while True:
    getal = input('Geef een getal: ')
    if int(getal) == 0:
        break

    getallen.append(int(getal))
print(f'Er zijn {len(getallen)} getallen ingevoerd, de som is: {sum(getallen)}')
"""

### 8.2 ###
"""
woord = input('Geef een string van vier letters: ')

while len(woord) != 4:
    print(f'{woord} heeft {len(woord)} letters')
    woord = input('Geef een string van vier letters: ')
    
print(f'Inlezen van correcte string: {woord} is geslaagd')
"""


### 8.3 ###
def hoogvliegers(dict_studenten_cijfers):
    res = []
    for item in dict_studenten_cijfers.items():
        if item[1] >= 9.0:
            res.append(item)
    return dict(res)


### 8.4 ###
def tickers_to_dict(filename):
    with open(filename, 'r') as file:
        companies = []
        for company in file.read().splitlines():
            companies.append(list(company.split(':')))
        return dict(companies)




def name_to_symbol(name, tickers):
    return tickers.get(name)


def symbol_to_name(symbol, tickers):
    return list(tickers.keys())[list(tickers.values()).index(symbol)]


tickers = tickers_to_dict('tickers.txt')

"""
name = input('Enter Company name: ')
print("Ticker symbol: {}".format(name_to_symbol(name, tickers)))

symbol = input('Enter Ticker symbol: ')
print("Company name: {}".format(symbol_to_name(symbol, tickers)))
"""


### 8.5 ###
def namen():
    """
    Neemt een lijst met namen, een geeft een dictionary terug met de namen als
    keys, en het aantal keer dat ze voorkomen in de lijst als waarden.

    :return: Een dictionary met namen en hoe vaak ze voorkomen.
    """
    namenlijst = []
    namendict = {}
    while True:
        naam = input('Volgende naam: ')
        if len(naam) > 0:
            namenlijst.append(naam)
        else:
            for naam in namenlijst:
                keys = naam
                values = namenlijst.count(naam)
                namendict[keys] = values
            break
    return namendict

