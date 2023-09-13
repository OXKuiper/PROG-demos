# Hier komt de demo van PROG3.
# Deze commit/push ik naar mijn voor jullie toegankelijke github repo na de les

### For loops ###
# Met for-loops kan je bijvoorbeeld over een lijst itereren
lijst = ['Cas','Wim','Bob','Eva','Mo']

for i in lijst:
    print('In de for-loop')
    print('Hoi', i) # i is de 1e keer 'Cas', daarna 'Wim' etc.

print('\nNa de for-loop')

### BMI voorbeeld ###
lengte = float(input('Geef je lengte: '))   # let op, input() geeft str terug, maak het float(), of int()
gewicht = float(input('Geef je gewicht: '))

BMI = gewicht / lengte**2

# Je kan deze if/elif/else boomstructuur op verschillende goede manieren maken!
if BMI < 18.5:
    print('Laag BMI')
elif BMI > 25.0:
    print('Hoog BMI')
else:
    print('Normaal BMI')

### Range ###

for i in range(6): # lijst van 0 tot 6.
    print(i)

for i in range(2,6): # lijst van 2 tot 6.
    print(i)

for i in range(2,6,2): # Lijst van 2 tot 6 met stapjes van 2.
    print(i)