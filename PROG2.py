# Demo les 2

user_input = input('Wat is je naam?')
print('Hoi, je heet: ' + user_input)

user_age = input('Wat is je leeftijd?')

# let op dat ook al vraag je een getal, user_age nu een str is!
print('Type van user_age is: ', type(user_age))

# om er mee te rekenen, moeten we er en int (of float) van maken, bijv:
user_age = int(user_age)

# Nu kunnen we:
user_age_times_two = user_age*2

print('Hoi, je bent als je twee keer zo oud bent ' + str(user_age_times_two))

#

# Je kan met print overigens + of , gebruiken om iets wat je wil printen op te bouwen
# Werk allebei, maar net anders:
# Met + maak je er één string van terwijl met , je aan print meerdere "argumenten" meegeeft
# Als we naar functies gaan kijken daarover meer. Voor nu: Kies een manier die voor jou werkt.

# Hieronder nog een voorbeeld van print() op verschillende manieren, die hetzelfde doen
my_name = 'Henk'
my_age = 66
print("Hoi " + my_name + " you are " + str(my_age) + " years old!")
print("Hoi", my_name, "you are", str(my_age), "years old!")

# # Extra fancy manier om te printen.
# print(f"Hoi {my_name} you are {my_age} years old!")







