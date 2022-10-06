### 6.1 ###
def convert(temp):
    return (temp * 1.8) + 32

def table():
    table = '{:^6}{:^12}'.format('F', 'C')
    for temp in range(-30, 50):
        if temp % 10 == 0:
            table = table + '\n{:^6}{:>8.1f}'.format(convert(temp), temp)

    return table

#print(table())

### 6.2 ###
def pretty_print():
    output = ''
    with open('kaartnummers.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            data = line.split(', ')
            output = output + data[1].replace("\n", "") + f' heeft kaartnummer: {data[0]}\n'
    return output

### 6.3 ###
def analyse():
    with open('kaartnummers.txt', 'r') as file:
        lines = file.readlines()
        hoogste_nummer =
        return f'Deze file telt {len(lines)} regels\nHet grootste kaartnummer is: {lines[-1]}'

print(analyse())