### Voorbeeld psycopg2 vanuit Python met SQL-database communiceren

# Installeer deze package nog niet hebt
import psycopg2

# Dit is extra, maar netjes om je passwords niet in je code te zetten
with open('Data/my_database_key.txt') as infile:
    passw = infile.read()

# Ik heb een Postgresql server draaien op mijn laptop, dus host='localhost'.
connection_string = f"host='localhost' dbname='PROG_demo' user='Ouren' password='{passw}'"

# get a connection with the database
conn = psycopg2.connect(connection_string)

# a ‘cursor’ allows to execute SQL in a db-session.
cursor = conn.cursor()

# multiline string ("""), no need to escape characters quotes, tabs, newlines
query = """SELECT * 
           FROM STUDENTS """

# a ‘cursor’ allows to execute SQL in a db-session
cursor.execute(query)
records = cursor.fetchall()
conn.close() # je kan ipv close() ook de connectie openen met with, dan hoeft dit niet.

# print the first column (klantnr) of each record
for record in records:
    print(record)

####################################
# Voorbeeld 2
naam = 'Henk'
conn = psycopg2.connect(connection_string)
cursor = conn.cursor()

query = """SELECT * 
           FROM STUDENTS
           WHERE name = %s ;"""
data1 = 'Henk'

# dit stopt de data uit data1 op de plekken van "%s". Let op dat (data1,) hier een tuple met 1 item maakt
cursor.execute(query, (data1,))
records = cursor.fetchall()				# retrieve the records from the database
conn.close()

print(records)


## VOORBEELD TRY EXCEPT

# dit kan werken... maar kan ook problemen geven!
strAge = input('Geef je leeftijd... als int plz☺ : ')
intAge = int(strAge)
print(f'You are {intAge} years old.')

# Zo vangen we potentiele problemen af
try:
    strAge = input('Geef je leeftijd: ')
    intAge = int(strAge)
    print(f'You are {intAge} years old.')
except:
    print('Gebruik alleen hele cijfers a.u.b.!')
