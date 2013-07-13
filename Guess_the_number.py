# "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

# Check it at http://www.codeskulptor.org/#user11_TRJmBQ0mSUEFh6B.py

import random
import simplegui

# initialize global variables used in your code

secret_number = None
number_guesses = None

# Helper functions

def init():
    range100()

# define event handlers for control panel
    
def range100():
    """ button that changes range to range [0,100) and restarts """
    
    global secret_number, number_guesses
    
    #Sets number of guesses
    number_guesses = 7
 
    #Generate secret number 
    secret_number = random.randrange(0, 100)
    
    #Prints out range of the game and number of guesses
    print "\nNew game in range from 0 to 100 is started! \nYour limited  number of guesses is", number_guesses

def range1000():
    """ button that changes range to range [0,1000) and restarts """
    
    global secret_number, number_guesses
    
    #Sets number of guesses
    number_guesses = 10
 
    #Generate secret number 
    secret_number = random.randrange(0, 1000)
    
    #Prints out range of the game and number of guesses
    print "\nNew game in range from 0 to 1000 is started! \nYour limited  number of guesses is", number_guesses
    

def validate_input(guess):
    """ Validate the input for digits and calls Main game logic """
    
    if guess.isdigit():
        get_input(guess)
        
    else:
        print "\nYour guess should be number! Try again!"
    
    
def get_input(guess):
    
    """ Main game logic """
    
    # Turns input from string to number
    guess = int(guess)
    
    # Decrement number of guesses
    global number_guesses   
    number_guesses -= 1
        
    # Determines the answers of first player(computer)
    if number_guesses == 0 and secret_number != guess:
        print "\nYou lost the game!"
        
        # Start new game
        range100()
        
    elif secret_number == guess:
        print "\nCorrect!"
        
        # Start new game 
        range100()
        
    elif secret_number > guess:
        print "\nHigher! \nNumber of remaining guesses is", number_guesses, "\nYour guess was", guess
   
    elif secret_number < guess:
        print "\nLower! \nNumber of remaining guesses is", number_guesses, "\nYour guess was", guess
    
# create frame

frame = simplegui.create_frame("Guess the number", 300, 200)

# register event handlers for control elements

frame.add_button("Range is [0, 100)", range100, 200)
frame.add_button("Range is [0, 1000)", range1000, 200)
frame.add_input("Enter a guess", validate_input, 200)

init()

# start frame
frame.start()
