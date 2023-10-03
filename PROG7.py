# Demo code van les 7 (PROG7)

#### DICTIONARIES ####
# Een dictionary bestaat uit allemaal key-value combinaties.
# Hier een dictionary met studenten en hun leeftijden
# Hier zijn de namen de 'keys' en de leeftijden de 'values'
studenten = {'Alice': 41, 'Bob': 33, 'Charles' : 20}

# Je kan op verschillende manieren met een for-loop dictionaries afgaan (bijvoorbeeld om iets te zoeken of te tellen)
for key, value in studenten.items():
    print(f'Key: {key} value: {value}')

# Je kan met blokhaken net als bij lijsten in dictionaries. Alleen ipv de index de 'key'.
print(f'Alice is: {studenten["Alice"]} jaar.')

# Of met hulp van blokhaken aanpassen, alice is een jaar ouder:
studenten['Alice'] += 1
print(studenten)

# Je kan ook makkelijk iets nieuws toevoegen aan dicts
studenten['Henk'] = 62
print(studenten)


## Voorbeeld van de slides wat je zoal kan met dicts

def complete(abbreviation):
    """returns day of the week corresponding to abbreviation"""

    if abbreviation == 'Mo':
        return 'Monday'
    elif abbreviation == 'Tu':
        return 'Tuesday'
    # elif                                  # Dit kan, maar is veel werk! Hieronder een oplossing met dicts
    #     ......
    else: # abbreviation must be Su
        return 'Sunday'

def complete(abbreviation):
    """returns day of the week corresponding to abbreviation"""
    days = {'Mo': 'Monday', 'Tu': 'Tuesday', 'We': 'Wednesday',
            'Th': 'Thursday', 'Fr': 'Friday', 'Sa': 'Saturday',
            'Su': 'Sunday'}
    return days[abbreviation]


### Voorbeeld uit slides
grades = [95, 96, 100, 85, 95, 90, 95, 100, 100]

# Ik wil kunnen zien hoeveel studenten 100 punten hebben gehaald.
# Maar niet steeds de lijst tellen (zeker als deze heel lang is)...


def frequency(itemList):
    """returns frequency of items in itemList"""
    counters = {}
    for item in itemList:
        if item in counters:
            counters[item] += 1  # add 1 to item counter
        else:
            counters[item] = 1  # create item counter
    return counters


dict_met_grades = frequency(grades)
print(dict_met_grades)
# Geeft {96: 1, 90: 1, 100: 3, 85: 1, 95: 3} # er waren dus 3 studenten met 100!


##### WOORDENTELLER #######
## Woordenteller uit de slides. Maar dan mooier, functie returned nu een dictionary
def wordCount(text):
    """Prints frequency of each word in text"""
    wordList = text.split()  # split text into list of words (on ' ' (spaces))

    counters = {}
    for word in wordList:
        if word in counters:
            counters[word] += 1  # counter for word exists, add 1 to its counter
        else:
            counters[word] = 1   # counter for word doesn't exist, create and set to 1
    return counters

uitkomst_dict = wordCount('all animals are equal but some animals are more equal than other')
print(uitkomst_dict)

# Extra: Je kan de uitkomst ook mooi printen (de slides deden dit origineel in de functie..)
for woord in uitkomst_dict:    # print word counts
    if uitkomst_dict[woord] == 1:
        print(f'{woord} appears 1 time.')
    else:
        print(f'{woord} appears {uitkomst_dict[woord]} times.')

# Voorbeeld uit slides... de key is hier een tuple (bijv ('Henk', 'Janssen'), een tuple met 2 items
telefoonboek = {('Henk', 'Janssen'): '0612345678',
                ('Mo', 'Bakker'):    '0687654321',
                ('Sean', 'Visser'):  '0612344321'}

# Ik zou zelf al key gewoon een uniek nummer/string gebruiken, niet iets complex als een lijst/tuple/dict


# Schrijven naar JSON bestand
import json
results = [{'name': 'John', 'result': 4.0},
           {'name': 'Frank', 'result': 7.0}]

with open('Data/results.json', 'w') as json_file:
    # kijk een wat indent doet door weghalen of andere waarde
    json.dump(results, json_file, indent=4)

