### OPGAVE ####

number1 = float(input("Getal 1: "))  # 1p input. Float/int beide goed.
number2 = float(input("Getal 2: "))
number3 = float(input("Getal 3: "))

lst = [number1, number2, number3]           # 3p list
lst.sort()                                  # 2p sort. Of mag ook met if's
print(f"Het middelste getal is: {lst[1]}")  # 1p uitvoer

### OPGAVE ####

string = input("Voer een string in: ")  # 1p input + var-decl.
omgekeerd = ""
for char in string:                # 3p for loop op str (met iets van een accumulator)
    omgekeerd = char + omgekeerd   # 2p omdraaien

print(f"Deze string omgekeerd: {omgekeerd}")  # 1p print

# Alternatief
omgekeerd = string[::-1]


### OPGAVE ####
def isPositiefEnKleinerDan(x, y):  # 1p correcte fuctie decl.
    if x>=0 and x<y:               # 2p return + 3p expressie
        return True
    else:
        return False

# Alternatief:
def isPositiefEnKleinerDan(x, y): # 1p correcte fuctie decl.
    return 0 <= x < y             # 2p return + 3p expressie (kan ook met meer if's)


### OPGAVE ####
#run_the_loop = True
result = 1
while True:  # 1p while / 1p accumulator / 1p input
    invoer = input("Voer een getal in: ")
    if invoer == "stop":   # 2p stoppen loop (kan ook met break)
        #run_the_loop = False
        break
    else:
        result = result * int(invoer) # 2p expressie
# 1p output result
print(f"Als je deze getallen vermenigvuldigt, is het resultaat: {result}")


### OPGAVE ####
import math  # geen punten + of - #
x1 = int(input("X-positie van coördinaat 1 (x1): "))  # 2p inlezen coörds
y1 = int(input("Y-positie van coördinaat 1 (y1): "))
x2 = int(input("X-positie van coördinaat 2 (x2): "))
y2 = int(input("Y-positie van coördinaat 2 (y2): "))

dist = math.sqrt(((x2-x1) ** 2) + ((y2-y1) ** 2)) # 4p berekenen formule
output = "Afstand tussen de coördinaten ({},{}) en ({},{}): {:.4f}"

print(output.format(x1, y1, x2, y2, dist))  # 2p uitvoer/afronding

