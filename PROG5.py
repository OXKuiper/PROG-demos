### Files openen

# open()
# 'r' (read) is default.
# 'w' is write. 'a' is append (toevoegen).
infile = open('Data/voorbeeld2.txt', 'r')
lines = infile.readlines()
print(lines)

# vergeet niet te close()'n! Of gebruik 'with'!
infile.close()

# Tip, je kan ook naar een file in een andere folder/map.
# Stel je hebt een projectmap met de mappen pyfiles en data
# dan kan je vanuit /pyfiles/PROG5.py naar data/voorbeeld.txt met:
#  open("../data/voorbeeld") . Het stukje "../" zegt zeg maar 'ga een map terug'.

## String methods (handige methoden om strings te bewerken)
s1 = 'Hoi Barry'
s2 = s1.replace('Hoi', 'Hai')
print(s2)  # geeft 'Hai Barry'

# Woorden in een zin tellen.
s = 'Dit is een zin met een bepaald aantal woorden.'
s_list = s.split() # split standaard op spaties, maar je kan ook op bijv commas splitsen
print(f'De lengte van de zin is: {len(s_list)}')

#
s = 'henk'
s = s.upper()  # in s zit nu 'HENK'

# list slices
lijst = ['appel', 'banaan', 'citroen', 'druif', 'ei']
print(lijst[0:3]) # geeft het nulde-tot-het-3e ding, dus 0e, 1e, 2e.
#          # hier zou dat ['appel', 'banaan', 'citroen'] teruggeven


# # schrijf een for-loop die over een lijst getallen loopt, alle even getallen print
#
# lijst = [1,2,3,4,5,6,7,8]
# #sum(lijst)
#
# for i in lijst:
#     print(f' is nu {i}')
#     if i % 2 == 0:
#         print(f'Dit getal is even: {i}')