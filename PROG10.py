# Scope/

# Deze variable staat niet in een functie,
# dus is een 'globale variabele
x = 5
print(f'Buiten de functie is x: {x}')

def doubler(y):
    x = 2
    print(f'In de functie is x: {x}, y: {y}')
    return x*y

dubbele = doubler(5)
print(dubbele)

# Let op dat dit* niet kan:
x = 5
print(f'Buiten de functie is x: {x}')

def doubler_2(y):
    print(x) # <---*dit kan niet
    x = 2    # <--tenzij je deze weghaald
    print(f'In de functie is x: {x}, y: {y}')
    return x*y
x = 5
print(doubler_2(5))

# Praktische tip:
# Geef je variabelen verschillende namen, voorkomt verwarring

# nog een voorbeeld van de slides:
def funct(b):   # funct has global scope, b has local scope
    a = 6       # this a has scope local to function call funct()
    return a*b  # this a is the local a

a = 0           # this a has global scope

print(f'funct(3) = {funct(3)}')
print(f'a is {a}')                 # global a is still 0

# Met .format is meer gedoe en minder leesbaar
# deze twee regels doen precies hetzelfde.
print(f'a is {a}')
print('a is {}'.format(a))

