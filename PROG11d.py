#### VOORBEELD GRID. Speel hier mee om het een beetje onder de knie te krijgen.

from tkinter import *
root = Tk()

button = Button(master=root, text=f'Button 1')
button.grid(row=1, column=1, padx=10, pady=10)  # verander row/colum/padx/pady eens en kijk wat er gebeurd

label = Label(master=root, text=f'Label 1')
label.grid(row=2, column=1, padx=10, pady=10)

button2 = Button(master=root, text=f'Button 2')
button2.grid(row=3, column=1, padx=10, pady=10)

label2 = Label(master=root, text=f'Label 2')
label2.grid(row=4, column=1, padx=10, pady=10)

root.mainloop()