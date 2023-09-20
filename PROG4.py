'''Hier komen de voorbeelden uit de les van PROG4.
# Deze commit/push ik naar mijn voor jullie toegankelijke github repo na de les'''

#### Functies ####
# "def" kan je gebruiken om zelf een functie te maken (def==definieren)

# een functie kan iets returnen. Dan evalueert deze tot bijv een getal, zoals len() die je al kent
# Kijk zelf maar eens wat de functie met een return als len() doet....
x = len(['ali','bob'])
#print(x)          # dit print 2

# .... en wat een functie als print() doet
# x = print('Hoi')  # dit print hoi
# print(x)          # dit print None! De print() functie heeft namelijk geen return.

## Dat lijkt een beetje op list methods (functies die bij objecten als lijsten horen)
## Die returnen vaak ook niets. Bijv .sort()
lst = [3,2,1]
lst.sort() # dit sorteert, zonder iets te (hoeven) returnen. Zo gebruik je .sort()

x = lst.sort() # dit is niet hoe je sort() moet gebruiken
#print(x) # dit geeft None

### Het verschil tussen functies die returnen en niet returnen is even wennen!

#### Laten we zelf wat functies maken ####
# Let op: functies aanmaken roept de functie nog niet aan: je zet alleen de functie klaar
# Een functie kan 0, 1, 2 of zo veel input argumenten/parameters hebben als je wil
# Een functie kan wel of niet iets return-en

# Functie zonder inputs en zonder return
def print_hoi():
    print('hoi!')

# functie zonder inputs en met een return
def geef_mooi_getal():
    return 42

# functie met 1 input parameter en een return
def dagen_naar_uren(dagen):
    return dagen * 8

# De functie moet altijd nog aangeroepen worden. Anders doet deze niets.
uren_persoon1 = dagen_naar_uren(8)
uren_persoon2 = dagen_naar_uren(6)

#in dit geval wijzen we wat dagen_naar_uren() returned toe aan variabelen
#die zouden we nog kunnen printen met print(uren_persoon1)



### Nog even waarom wel/niet print

def wortel_print(getal):
    wortel = getal**0.5
    print(wortel)

def wortel_return(getal):
    wortel = getal**0.5
    return wortel


w_print = wortel_print(25)   # let op,deze functie returned helemaal niet
w_return = wortel_return(25) # deze functie returned wel, dus toekennen aan variabele is zinnig

## stel ik wil van een getal de wortel, keer twee.
## print(f'{w_print*2})') # dit geeft een foutmelding want w_print is None
#print(f'{w_return*2})') # dit werkt wel


# Een comment met ''' ''' aan het begin van de functie heet een "docstring"
def my_sqrt(number):
    """This function returns the square root of the number"""
    return number**0.5

## prints info on function.
# help(my_sqrt)

## kijk ook eens naar andere functies:
# help(abs)



## Slide over Assignment and mutability. Voorbeeld

lijst_1 = [5,3,1]
lijst_2 = lijst_1  # beide variabelen verwijzen nu naar het (list) object [5,3,1] !

lijst_1.sort() # dit sorteert de 'achterliggende' lijst!
               # Dus waar zowel lijst_1 als lijst_2 naar verwijzen!

# print(lijst_1, lijst_2) # zelfde (aangepaste) lijst!




## Meer over print()
w1 = 'Kip'
w2 = 'Paard'
w3 = 'Koe'
# print(w1,w2,w3, sep="    en een    ", end="!\n")  # end is standaard aleen \n, ofwel "newline" ofwel nieuwe regel
#
# print('ja',end='')
# print('ja',end='')
# print('ja',end='') # alle drie op een regel want end is niet meer \n
#
# print('') # lege print, print dus wel nog een \n  (nieuwe regel)

## Fancy fstrings bij print()
day = 'Wednesday'
month = 'March'
weekday = 'Wednesday'
day = 8
year = 2023
hour = 11
minute = 45
second = 33
# print(f'{hour}:{minute}:{second}')
# print(f'{weekday}, {month} {day}, {year} at {hour}:{minute}:{second}')

# Met f-strings hoef je niet str() te doen voor je variabelen met getallen, handig



## For loop, met range, met f-string-print
# for i in range(1, 8):
#     # :3 zorgt steeds voor 3 spaties gereserveerd
#     print(f'i={i}    i^2={i**2:3}     2^i={2**i:3}')

# afronden met fstring
x = 3.141592653589793238462643383279502884197
# print(f'{x:.2f}')

lst = ['Alexander Turing', 'Ken Yu', 'Vincent Cerf']
# Dit geeft de voornaam en achternaam terug op een mooie manier.
for name in lst:
    # dit is lelijk:
    print(name)
    # Mooier printen:
    #fl = name.split() # split werkt standaard op spaties, maar je kan ook op commas splitsen
    ## Tip, kijk een wat name.split() doet door hier te doen: print(fl)
    #print(f'{fl[0]:11} {fl[1]:11}')

# in het algemeen, knip de uitwerkingen van oefenopgaven even op in stukjes
# en kijk of je snapt wat de losse stukjes doen, ipv als geheel naar de code te kijken.