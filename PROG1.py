# Voorbeelden les 1 
# Dit is niet alle stof, maar mogelijk een handige aanvulling.

# Wat uitleg over python/pycharm in het algemeen:
# Alles wat je hier leest, zijn comments, omdat de regel start met een hekje(#)
# Voor Python zijn deze regels onzichtbaar

# Naast een hekje is ook text tussen ''' ''' een comment:
'''
  Dit is ook comment, en geen code.
  In PyCharm werk je altijd in een project, daarin heb je mappen, en vooral .py-files
  We zitten nu in een .py-bestand.

  Een .py kan je uitvoeren (voer je uit) met ctrl+shift+f10.
  Let op dat het start-icoon ook je .py file uitvoert, maar soms niet die je open hebt

  Een .py file voert uit in zijn geheel, van boven naar beneden.
  Later ga je zien dat je .py bestanden elkaar kunnen aanroepen voor complexere projecten.
'''

# Ok, lets go verder:
# tip, ctrl+/ om meerdere regels weg/te commenten.
# Zo heeft PyCharm veel handige keyboard shortcuts

# We werken nu in .py-bestanden,
# Je kan ook in de Python Console per regel python gebruiken (te herkennen aan >>>)
# Daarin als je bijvoorbeeld 2+2 doet, zie je de uitkomst (4), maar in pycharm:
2+2
# Geeft bovenstaande geen output! Je moet er nog iets mee doen.
# Wil je het afdrukken in het scherm hieronder? Dan zou je print(2+2) moeten doen
print(2+2)
# Later kijken we hoe je output van je code ook kan wegschrijven in bestanden, zodat je een echte applicatie kan bouwen

# VANAF HIER MOET JE ZELF print() TOEVOEGEN (of de regel un-commenten) ALS JE WIL ZIEN WAT ER UIT DE CODE KOMT

# OK! Nu gaan we eens kijken naar variabelen
x = 10
x = 20
x # de variabele 'x' bevat hier de integer 20. (vergeet print() niet als je het wil zien)

# Je kan python waardes/objecten toekennen aan variabelen.
# Variabelen zijn... variabel.
# Misschien is voor de ene gebruiker de variabele klant_nummer wel 80085, en voor de andere klant 12345.

# Met type() kan je makkelijk achterhalen wat het datatype is van waar je variabele naar verwijst.
type(x) # dit geeft 'int' terug, van integer (heel getal)

# Strings hebben iets van aanhalingstekings nodig '' of ""

x = 'hoi' # dit kent de string 'hoi' toe aan de variabele x


# Ok! Nog wat meer info
## Python heeft ook 'indentation', dat is inspringen
print('hoi')
#    print('oh oh') # dit geeft een fout als je het hekje weghaalt. Let dus op spaces/tabs


x = 1
y = 2/2
#print(x) # geeft 1 terug
#print(y) # geeft 1.0 terug

# waarom geeft dit net iets anders terug? Antword: y is hier een float (getal met decimalen)
# Let op dat je met python niet altijd weet met welk data-type je werkt

# Let verder op dat je mogelijk nog dingen in een print() moet zetten om te kunnen inziet wat onderstaande code precies doet.

# Lijsten in python zijn heel handig
lijst = ['Hond','Kat','Vis','Otter']

# lijsten beginnen met tellen met plek-0, plek-1, plek-2, etc (de 'index')
lijst[0] # geeft het 0-e ding, dus hier 'Hond'!
lijst[1] # dit zou hier 'Kat' teruggeven als je het print

# op lijsten kan je handige functies toepassen, zoals len() voor de lengte
# of methodes, zoals .sorted() om de lijst te sorteren

# let op dat len(lijst) echt iets teruggeeft, dus je wil bijv doen:
lengte = len(lijst)
# methoden doen soms gewoon iets, zoals
lijst.sort()
# Hier hoef je verder niets aan te doen! De list 'lijst' is nu gesorteerd in het geheugen van python.
#print(lijst)

# Lijste kan je aanpassen
lijst[1] = 'Tijger' # Het ding op index 1 (het 2e ding!) wordt 'Tijger' (het was eerst 'Kat', wat een upgrade)
#print(lijst)

# Tuples zijn lijsten, maar dan onveranderlijk.
primaire_kleuren = ('groen','rood','blauw')

# primaire_kleuren[1] = 'paars' # Dit zou een fout geven!

# laten we even naar booleans kijken!
# Booleans zijn ofwel True ofwel False. Hoofdletter maakt uit.

#(3 == 3) # geeft True, want 3 is inderdaad gelijk aan 3.

#print(2 > 3) # geeft False, want 2 is niet groter dan 3.

#print(3 > 2 and 5 > 8) # Geeft True. als links én recht van and True staat, is het geheel True.

# De rest kan je zelf uitproberen a.d.h.v. de slides!

# Dit soort dingen zijn soms lastig te lezen
x = 3 + 2 == 2
# Er zit volgorde in wat python doet! Rekenen gaat voor de boolean-dingen (==) enzo,

# het toekennen aan variabelen (met =) gaat altijd als laasts
x =  244%2==0 or 244//3 > 100

# Je kan ook haakjes zeten om de volgorde aan te passen van wat eerst gebeurd.

# Let op dat je per ongeluk KAN rekenen met True/False, dan zijn ze 1 en 0...
# Maar dit maakt je code onleesbaar

#print( ( 100 > 50) + 1) # dit geeft 2 terug... Maar slaat niet echt ergens op!

# probeer ook vooral zelf uit om te zien wat de volgorde is van arithmetic (rekenen) en boolean expressions


# Laten we even naar string kijken!
# ' '
s = 'abcdefg'
s[0] # 1e character, dus 'a'
s[-1] # laatste character, dus 'g'
'abc' in s # zegt True/False of 'abc' in string s zit

## Meer voorbeelden list methods/functions
# waardes = [1, 3, 2, 1, 3]
# ## dit zijn methoden die je op het type list kan uitvoeren.
# waardes.append(4)
# waardes.count(3)
# waardes.remove(2)
# waardes.reverse()
# waardes.index(3)
# waardes.sort()
## dit zijn functies met de lijst als input
# len(waardes)
# max(waardes)

## Je kan lijsten vullen met vanalles! Maar is meestal niet zinvol:
l = ['Henk',200,1314132]


''' 
Blijf lekker dingen zelf uitproberen!

Succes!
'''