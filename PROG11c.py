# Buttons voorbeeld!

import tkinter as tk

def get_entries():
    value1 = entry1.get()
    value2 = entry2.get()
    result_label.config(text=f"Getallen keer elkaar: {float(value1) * float(value2)}")

root = tk.Tk()
root.title("Voorbeeld met twee velden")

label = tk.Label(master=root, text='Vul twee getallen in', height=2)
label.pack()

entry1 = tk.Entry(root)
entry2 = tk.Entry(root)

entry1.pack()
entry2.pack()

submit_button = tk.Button(root, text="Submit", command=get_entries)
submit_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()