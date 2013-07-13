# Mini-project #6 - Blackjack
# Check it at http://www.codeskulptor.org/#user15_PhjL7FUUtX6KSR9.py

import simplegui
import random

# load card sprite - 949x392 - source: jfitz.com
CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0

card_deck = []
player_hand = []
dealer_hand = []
wins = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.player_hand = []	# create Hand object

    def __str__(self):
        return 'Hand contains: %s' % ' '.join([str(i) for i in self.player_hand])	# return a string representation of a hand

    def add_card(self, card):
        self.player_hand.append(card)	# add a card object to a hand

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        # compute the value of the hand, see Blackjack video
        sum_list_values = sum([VALUES[i.rank] for i in self.player_hand])

        count_aces = len([VALUES[i.rank] for i in self.player_hand if i.rank == "A"])

        while sum_list_values < 21 and count_aces != 0:
            if sum_list_values <= 11 and count_aces > 0:
                sum_list_values += 10
            count_aces -= 1
        
        return sum_list_values	
   
    def draw(self,canvas, pos): # draw a hand on the canvas, use the draw method for cards
        for c in self.player_hand:
            pos[0] = pos[0] + 100
            c.draw(canvas, pos)

 
        
# define deck class 
class Deck: 
    def __init__(self): # create a Deck object
        self.deck = []
        for suit in SUITS:
            for rank in RANKS:
                self.deck.append(Card(suit, rank))

    def shuffle(self):
        # add cards back to deck and shuffle
        random.shuffle(self.deck) # use random.shuffle() to shuffle the deck

    def deal_card(self):
        # deal a card object from the deck
        return self.deck.pop(0)
    
    def __str__(self):
        return 'Deck contains: %s' % ' '.join([str(i) for i in self.deck])

#define event handlers for buttons
def deal():
    global outcome, in_play, card_deck, player_hand, dealer_hand
    #create card deck
    card_deck = Deck()
    
    #shufle card deck
    card_deck.shuffle()
    
    # Creates player and dealer hands
    player_hand = Hand()
    dealer_hand = Hand()
    
    #add two cards to player hand
    for i in range(2):
        transfered_card = card_deck.deal_card()
        player_hand.add_card(transfered_card)
    
    #add two cards to dealer hand
    for i in range(2):
        transfered_card = card_deck.deal_card()
        dealer_hand.add_card(transfered_card)

    in_play = True
    
    print  'Player: %s value %s' % player_hand, player_hand.get_value()
    print  'Dealer: %s value %s' % dealer_hand, dealer_hand.get_value()
    

def hit():
    global outcome, wins, in_play
    # Prevent hitting Hit button if player busted
    if player_hand.get_value() > 21:
        return
    
    #adds one more card to player hand
    transfered_card = card_deck.deal_card()
    player_hand.add_card(transfered_card)
    
    print  'Player: %s value %s' % player_hand, player_hand.get_value()
    
    if player_hand.get_value() > 21:
        in_play = False
        wins -= 1 
        outcome = "You have busted!"
        
    # if the hand is in play, hit the player
   
    # if busted, assign a message to outcome, update in_play and score
       
def stand():
    global outcome, wins, in_play
    # Prevent hitting Hit button if dealer busted
    #if dealer_hand.get_value() > 21:
        #return
    
    # If the player has busted, remind the player.
    if player_hand.get_value() > 21:
        outcome = "You have busted!"
        return
    
    while dealer_hand.get_value() < 17:
        transfered_card = card_deck.deal_card()
        dealer_hand.add_card(transfered_card)
    
    if dealer_hand.get_value() > 21:
        #print 'dealer: %s value %s' % dealer_hand, dealer_hand.get_value()
        in_play = False
        outcome = 'Dealer have busted!'
        
    if dealer_hand.get_value() > player_hand.get_value() and dealer_hand.get_value() < 0:
        wins -= 1 
        in_play = False
        outcome = "Dealer wins"
    elif dealer_hand.get_value() == player_hand.get_value():
        in_play = False
        outcome = "Plyer and Dealer are equal!"
    else:
        in_play = False
        wins += 1
        outcome = "Player wins"
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more

    # assign a message to outcome, update in_play and score

# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    canvas.draw_text("Blackjack", (50, 50), 45, "White")
    #card = Card("S", "A")
    #card.draw(canvas, [300, 300])
    canvas.draw_text("Dealer", (50, 130), 30, "White")
    dealer_hand.draw(canvas, [0,150])
    
    canvas.draw_text("Player", (50, 380), 30, "White")
    player_hand.draw(canvas, [0,400])
    
    canvas.draw_text(outcome, (200, 320), 30, "White")    
    
    canvas.draw_text("Score", (400, 120), 20, "White")
    canvas.draw_text(str(wins), (400, 140), 20, "White")
    
    if in_play:
        canvas.draw_image(card_back, (50,50), CARD_BACK_CENTER, (135,200), CARD_BACK_SIZE)
      
 
# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
frame.start()
deal()
# remember to review the gradic rubric