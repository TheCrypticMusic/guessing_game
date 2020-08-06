from tkinter import *
import random

num = random.randint(1, 20)



def user_guess(event=None):
    choice = guess.get()
    if int(choice) == num:
        print('True')
    else:
        print('False')


#def higher_or_lower():
    #if user_guess():
        #return 'Number is lower'
    #else:
        #return 'Number is higher'

root = Tk()
root.title('Guessing Game')
root.geometry('400x200')    

Label(root, text='RULES OF THE GAME\n\n\
    You have 5 turns to guess the number between 1 - 20.',).pack(side=TOP, pady=5)

Label(root, text=f'Test').pack(pady=10)

guess = Entry(root)
guess.bind('<Return>', user_guess)
guess.pack(side=TOP, pady=5)


root.mainloop()

