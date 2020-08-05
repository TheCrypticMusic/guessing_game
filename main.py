import random as r 

def random_number():
    return r.randint(1, 20)

def user_choice():
    while True:
        try:    
            user_input = int(input('Please enter a number (1 - 20): '))
            if user_input == random_number():
                print('Correct')
                break
            else:
                print('Wrong')
        except ValueError:
            print("ENTER A NUMBER")



random_number()
user_choice()