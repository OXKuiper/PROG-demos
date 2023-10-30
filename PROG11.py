''' Het basic TKinter voorbeeld '''

''' Importeren TKinter.

Als je niet steeds tkinter.[iets] wil typen, bijvoorbeeld tkinter.tk() kan je ook doen:

import tkinter as tk

Dan kan je voortaan zeggen tk.Tk() bijvoorbeeld

of als je gewoon alle functies tot je beschikking wil hebben zonder de module expliciet te noemen:
'''

from tkinter import *

# Tk() komt vanuit de tkinter module. Nadeel, nu lastig te 'zien', je moet het weten
# Tk() is... een schermpje. Verder nog niets.
root = Tk()

# Om die te runnen.... gebruiken we .mainloop()
root.mainloop()


root = Tk()
label = Label(master=root,
              text='Hello World',
              background='yellow')
label.pack()
root.mainloop()

######

root = Tk()
label = Label(master=root,
                text='Hello World',
                    background='yellow',
                    foreground='blue',
                    font=('Helvetica', 16, 'bold italic'),
                    width=15,
                    height=8)
label.pack()
root.mainloop()



from tkinter import *
root = Tk()
img = PhotoImage(file='Data/beach.png')
label = Label(master=root, image=img)
label.pack()
root.mainloop()
