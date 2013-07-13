# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# Check it out at http://www.codeskulptor.org/#user10_WDKonEWJwTImEJY_2.py


import random

# helper functions

def name_to_number(name):
    """ Converts the string name into a number between 0 and 4 """
    
    if name == "rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    else:
        return "Wrong sign thrown! Please choose again!"

def number_to_name(number):
    """ Converts a number in the range 0 to 4 into its corresponding name as a string """
    
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"
    else:
        return "Wrong number input!"

def rpsls(player_guess):
    """ Determines and prints out the winner """
    
    # convert name to player_number using name_to_number
    
    player_number = name_to_number(player_guess)

    # compute random guess for comp_number using random.randrange()
    
    comp_number = random.randrange(0, 5)
    
    #comp_number = 2
    
    # Converts a computer random number into its corresponding name as a string
    
    computer_guess = number_to_name(comp_number)

    # compute difference of player_number and comp_number modulo five
    
    players_difference = (player_number - comp_number)%5

    # use if/elif/else to determine winner
    
    if players_difference <= 2 and players_difference > 0:
        winner = "Player wins!"
    elif players_difference > 2:
        winner = "Computer wins!"
    elif players_difference == 0:
        winner = "Player and computer tie!"
    else:
        winner = "Wrong modular arithmetic!"
    
    # print results
    
    print "Player chooses", player_guess, "\n", "Computer chooses", computer_guess, "\n", winner, "\n"

    
# test your code
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
