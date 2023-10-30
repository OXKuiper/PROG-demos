''' Het iets uitgebreidre TKinter voorbeeld (Buttons)'''


from tkinter import *

# functie die later gebruikt wordt door hem aan de Button 'button' te koppelen
def onclick():
    label["text"] = entry.get() # dit past een label aan, maar kan vanalles doen

def onclick2():
    base = int(entry.get())
    square = base ** 2
    outcome = f"square: of {base} = {square}"
    label["text"] = outcome

root = Tk()
label = Label(master=root, text='Geef een getal, dan krijg je het kwadraad', height=2)
label.pack()
button = Button(master=root, text='Press', command=onclick2)  # NIET onclick() !!!

button.pack(pady=10)  # pady is pad y. 'to pad' is opvullen (opschuiven).

entry = Entry(master=root)
entry.pack(padx=10, pady=10)

root.mainloop()


