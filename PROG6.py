# Demo code voor prog 6

# slide 3/4

pets = ['cat', 'dog', 'fish', 'bird']

# Je kan een lijst afgaan per item. Je noemt de variabele dan naar het ding (hier: animal).
for animal in pets:
    print(animal) # print een voor een ieder dier in de lijst

pets = ['cat', 'dog', 'fish', 'bird']
# Je kan een lijst afgaan via de index (plek). Dus 0, 1, ... tot de lengte vd lijst. Variabelenaam i is dan gebruikelijk.
for i in range(len(pets)):
    print(f'\nIn de for loop is variabele i nu: {i}')
    print(f'En dat is dier: {pets[i]}') # vaak op deze manier gebruikt

    # Omdat je de index weet, kan je bijv:
    if pets[i] == 'fish':
        print(f'Fish staat op plek {i} in de lijst')

## ALTERNATIEVE MANIER - Enumerate om gelijk item zelf én index te hebben
for i, animal in enumerate(pets):  # ennumerate geeft een soort dubbele-lijst, van de index en wat er daadwerkelijk in de lijst zit.
    print(f'Nu is i en animal: {i} en {animal}')


# Slide 8. Nested loop.
# Voorbeeld op de slide is erg onduidelijk. Dit is denk ik duidelijker:
# Stel je hebt een lijst van woorden, en je wil iedere letter 'a' een 'A' maken
# Dat kan met een loop-in-een-loop nodig. Namelijk:
# Je wil alle woorden afgaan. (for-loop 1)
#    Je wil alle letters per woord afgaan. (for-loop 2)

pets = ['cat', 'dog', 'fish', 'bird', 'giraffe']
pets_2 = []
for word in pets:
    new_word = ""
    for letter in word:
        if letter == 'a':
            new_word += 'A'
        else:
            new_word += letter
    pets_2.append(new_word)

print(pets_2)

pets = ['catfish', 'dog', 'fish', 'bird', 'giraffe']
print(pets[0][0:4])  # Dit pakt eerst het 0e ding, daarna de eerste 3 elementen. Dus hier 'cat'



### Slides over two dimensional lists
# Boter-kaas-eieren maken? Dat kunnen we nu!
# Misschien vind je het zelf leuk om dit af te maken? Ga ervoor!

# 0 is leeg, 1 is speler1, 2 is speler2
boter_kaas_eieren = [[0,0,0],
                     [0,0,0],
                     [0,0,0]]  # startstaat van het bord (leeg)
game_on = False  # zet op true om te spelen. to-do nu nog geen stop-manier.. wat zou die kunnen zijn?
speler = 1      # startspeler
while game_on:
    user_in = input(f'Speler {speler} Waar wil je een teken zetten? (Gebruik: rij, kolom)')
    x,y = user_in.split(',')
    print(f'Je koos plek {x},{y}')
    if boter_kaas_eieren[int(x)][int(y)] != 0: # niet leeg
        print('Je kan niet op een al gevuld veld iets invullen!')
        continue

    # vul veld in
    boter_kaas_eieren[int(x)][int(y)] = speler # vul met huidige speler

    # hier code om te checken of iemand heeft gewonnen (tip: best lastig)
    # to-do...

    # hier een check of het veld niet vol is (en dus gelijkspel als je kijkt na de victory-check
    # to-do...

    # switch speler die aa de beurt his
    if speler == 1:
        speler = 2
    else:
        speler = 1

    # manier om je grid te printen
    for i in boter_kaas_eieren:
        for j in i:
            print(j, end='')
        print('')


### Continue and break
# Continue zegt eigenlijk: Rond deze loop af gelijk en ga door naar de volgende
for i in range(5):
    if i == 2:
        continue
    print(i) # als i==2 wordt deze regel niét uitgevoerd (wel weer als i een ander getal is)

# Break zegt: we zijn klaar met het hele for-lopen
for i in range(5):
    if i == 2:
        break
    print(i) # als i==2 wordt deze regel niét uitgevoerd.. EN later ook niet, want de hele for-loop is klaar

### while loop met stop conditie
geld = 10
maanden = 0
while geld < 1000:
    geld = geld * 1.05 # iedere maand %5 rente erbij.
    maanden = maanden + 1
    print(f'Na {maanden} maanden is mijn totale geld {geld:.2f}')

