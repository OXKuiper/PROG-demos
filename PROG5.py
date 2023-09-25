### Democode uit les 5.

### Files openen

# open()
# 'r' (read) is default.
# 'w' is write. 'a' is append (toevoegen).
infile = open('Data/voorbeeld2.txt', 'r')
lines = infile.readlines()
print(lines)

# vergeet niet te close()'n! Of gebruik 'with'!
infile.close()

# open met with voorbeeld:
with open('Data/voorbeeld2.txt') as infile:
    lines = infile.readlines()
    print(lines)
    # aan het einde doet hij dankzij with close() vanzelf

# Tip, je kan ook naar een file in een andere folder/map.
# Stel je hebt een projectmap met de mappen: pyfiles en data
# dan kan je als je werk in /pyfiles/PROG5.py naar data/voorbeeld.txt met:
#  open("../data/voorbeeld") . Het stukje "../" zegt zeg maar 'ga een map terug'.


## String methods (handige methoden om strings te bewerken)
s1 = 'Hoi Barry'
s2 = s1.replace('Hoi', 'Hai')
print(s2)  # geeft 'Hai Barry'

# nog een voorbeeld
input1 = 'Hoi, ik, ben, een NS reiziger en bla'
lijst = input1.split(',')
print(f'Het aantal woorden in de lijst is {len(lijst)}')


#
s = 'henk'
s = s.upper()  # in s zit nu 'HENK'

# list slices
lijst = ['appel', 'banaan', 'citroen', 'druif', 'ei']
print(lijst[0:3]) # geeft het nulde-tot-het-3e ding, dus 0e, 1e, 2e.
#          # hier zou dat ['appel', 'banaan', 'citroen'] teruggeven


# # schrijf een for-loop die over een lijst getallen loopt, alle even getallen print
#
# lijst = [0,1,2,3,4,5,6,7,8]
#
# for i in lijst:
#     print(f' is nu {i}') # altijd goed om even te checken wat je for-loop in de basis doet door te kijken wat i steeds is, en hoe vaak deze wordt uitgevoerd
#     if i % 2 == 0:
#         print(f'Dit getal is even: {i}')