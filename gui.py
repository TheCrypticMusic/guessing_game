from tkinter import *
from main import random_number


num = random_number()  

def user_guess(event=None):
    if int(guess.get()) == num:
        print('Correct')
    else:
        print('Incorrect')


root = Tk()
root.title('Guessing Game')
root.geometry('400x200')    

Label(root, text='RULES OF THE GAME\n\n\
    You have 5 turns to guess the number between 1 - 20.',).pack(side=TOP)

Label(root, text=f'{num}').pack(pady=10)

guess = Entry(root)
guess.bind('<Return>', user_guess)
guess.pack(side=TOP, pady=5)



root.mainloop()
