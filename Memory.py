# implementation of card game - Memory
# The goal is to open all the maching pair cards
# Check it at http://www.codeskulptor.org/#user14_Y8sWiFLAyt_6.py

import simplegui
import random

state = 1
card_exposed = None
prev_card_exposed = None
click_counter = 0

# helper function to initialize globals
def init():
    global deck_cards, exposed, card_exposed, prev_card_exposed, click_counter
    
    # Create and shuffle the deck of cards
    deck_cards = range(1, 9)
    deck_cards = deck_cards + deck_cards
    random.shuffle(deck_cards)
    
    # Creates list full with Fals values
    exposed = [x==False for x in range(1, 17)]
    
    # Resets all global variables
    card_exposed = None
    prev_card_exposed = None
    click_counter = 0

# define event handlers
def mouseclick(pos):
    # add game state logic here
    global card_exposed, prev_card_exposed, state, exposed, click_counter
    
    # get the index of the clicked card
    card_exposed = pos[0]//50
    
    #double_click = None
    #if card_exposed == double_click:
        #return
    #double_click = card_exposed
    
    # counts the tries of the player
    click_counter = click_counter + 1
    label.set_text("Moves = " + str(click_counter))
        
    if state == 1:
        prev_card_exposed = card_exposed
        state = 2
    else:
        state = 1
        if deck_cards[card_exposed] == deck_cards[prev_card_exposed]:
            exposed[card_exposed] = True
            exposed[prev_card_exposed] = True
        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global prev_card_exposed, exposed
    
    # If there aren't currently faced up cards and mached pairs draws greeen backgrounds
    for cards_unexposed in range(len(deck_cards)):
        
        if card_exposed != cards_unexposed and prev_card_exposed != cards_unexposed and not exposed[cards_unexposed]:
            canvas.draw_polygon([(0 + 50*cards_unexposed, 0), (50 + 50*cards_unexposed, 0), (50 + 50*cards_unexposed, 100),(0 + 50*cards_unexposed, 100)], 1, "Black", "Green")
        else:
            canvas.draw_text(str(deck_cards[card_exposed]),(50*card_exposed+15, 60), 40, "White")
            canvas.draw_text(str(deck_cards[prev_card_exposed]),(50*prev_card_exposed+15, 60), 40, "White")
    
    # Prints the matched pairs 
    for n in range(len(exposed)):
        if exposed[n]:
            canvas.draw_text(str(deck_cards[n]),(50*n+15, 60), 40, "White")
    
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Restart", init)
label = frame.add_label("Moves = 0")

# initialize global variables
init()

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
frame.start()
init()
# Always remember to review the grading rubric