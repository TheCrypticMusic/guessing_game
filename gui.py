from tkinter import *
from main import random_number


root = Tk()
root.title('Guessing Game')
root.geometry('400x200')

Label(root, text='RULES OF THE GAME\n\n\
    You have 5 turns to guess the number between 1 - 20.',).pack(side=TOP)

Label(root, text='ENTER A NUMBER').pack(pady=10)

entry = Entry(root)
entry.bind("<Return>")
entry.pack(side=TOP, pady=5)


root.mainloop()