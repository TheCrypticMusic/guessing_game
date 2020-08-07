from tkinter import *
import random

def random_number():
from tkinter import *
import random as rand

num = rand.randint(1, 20)
number_of_guesses = 0
score = 0

# TODO: FIX LOGIC TO MAKE NUMBERS REFRESH WHEN RESTART IS PRESSED

        
def restart_game():
    global number_of_guesses
    global score
    number_of_guesses = -1
    score = 0
    label['text'] = 'Enter a number'


def restart_button():
    restart_button = Button(root, text='RESTART', command=restart_game)
    restart_button.pack(pady=25)

def game(event=None):
    global num
    global number_of_guesses
    global score
    try:        
        if int(user_entry.get()) == num:
            # TESTING
            print(f'CORRECT: {num}')
            
            num = rand.randint(1, 20)
            label['text'] = 'Correct'
            number_of_guesses = -1
            score += 1
            score_count['text'] = f'Score\n{score}' 
            
        elif int(user_entry.get()) < num:
            # TESTING
            print(f'Number is higher: {num}')
            
            label['text'] = 'The number is higher'
            
        else:
            # TESTING
            print(f'Number is lower: {num}')
            
            label['text'] = 'The number is lower'
        number_of_guesses += 1
        guess_count['text'] = f'Guesses:\n{number_of_guesses}'
        if number_of_guesses == 5:
            restart_button()
            label['text'] = 'Game Over'
            
            
    except ValueError:
        label['text'] = 'ENTER A NUMBER'



    
root = Tk()
root.title('Guessing Game')
root.geometry('400x200')    

Label(root, text='RULES OF THE GAME\n\n\
    You have 5 turns to guess the number between 1 - 20.',).pack(side=TOP)

label = Label(root, text='Enter a number')
label.pack(pady=10)


user_entry = Entry(root)
user_entry.bind('<Return>', game)
user_entry.pack(side=TOP, pady=5, ipadx=30)

guess_count = Label(root, text=f'Guesses:\n{number_of_guesses}')
guess_count.pack(side=LEFT, padx=60)

score_count = Label(root, text=f'Score\n{score}')
score_count.pack(side=RIGHT, padx=60)


root.mainloop()
