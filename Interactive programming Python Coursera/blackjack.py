# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0


# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    global in_play
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
        if in_play:
            canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
            canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE,(65,240), CARD_BACK_SIZE)
        else:
            canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
            
# define hand class
class Hand:
    def __init__(self):
        self.Card = []

    def __str__(self):
        # return a string representation of a hand
        answ = ""
        for card in self.Card:
            answ += str(card) +' '
        return 'Hand contains '+answ

    def add_card(self, card):
        self.Card.append(card)	# add a card object to a hand

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        # compute the value of the hand, see Blackjack video
        value = 0
        for card in self.Card:
            value += VALUES[card.get_rank()]
        for card in self.Card:
            if 'A' in card.get_rank():
                if value + 10 <=21:
                    return value+10   
        return value
   
    def draw(self, canvas, pos):
       
       
        # draw a hand on the canvas, use the draw method for cards
       
        for i in range(len(self.Card)):
            self.Card[i].draw(canvas, pos)
            pos[0] += 100
            
        
# define deck class 
class Deck:
    def __init__(self):
        self.Card = []
        for suit in SUITS: 
            for rank in RANKS:
                self.Card.append(Card(suit,rank))

    def shuffle(self):
        # shuffle the deck 
        random.shuffle(self.Card)

    def deal_card(self):
        # deal a card object from the deck
        c = self.Card[-1]
        self.Card.pop()
        return c
        
    def __str__(self):
        answ = ""
        for card in self.Card:
            answ += str(card) +' '
        return 'Deck contains '+answ



#define event handlers for buttons
def deal():
    global outcome, in_play, score
    global dealer_hand, deck, player_hand
    outcome = ""    
    dealer_hand = Hand()
    deck = Deck()
    player_hand = Hand()
    # shuffle the deck
    
    if in_play:                    
            outcome ="You lose"
            score -=1
            deck.shuffle()
        # add 2 cards to each hand (dealer and player)
            dealer_hand.add_card(deck.deal_card())
            dealer_hand.add_card(deck.deal_card())
            player_hand.add_card(deck.deal_card())
            player_hand.add_card(deck.deal_card())
            in_play = False
    else:
            deck.shuffle()
        # add 2 cards to each hand (dealer and player)
            dealer_hand.add_card(deck.deal_card())
            dealer_hand.add_card(deck.deal_card())
            player_hand.add_card(deck.deal_card())
            player_hand.add_card(deck.deal_card()) 
            in_play = True
            
        

def hit():
      # replace with your code below
    global outcome, in_play, score
    global player_hand, deck
    if in_play:
        if player_hand.get_value() <= 21:
            player_hand.add_card(deck.deal_card())
            if player_hand.get_value()>21:
                outcome = "You have busted"
                in_play = False
                score -=1
 
    # if the hand is in play, hit the player
   
    # if busted, assign a message to outcome, update in_play and score
       
def stand():
    global outcome, in_play, score   # replace with your code below
    global dealer_hand, deck, player_hand
    if outcome == "You have busted. You lose":
        print outcome
    if in_play:
        while dealer_hand.get_value()<17:
            dealer_hand.add_card(deck.deal_card())
        if dealer_hand.get_value() > 21:
                outcome="dealer busts.You win"
                score +=1
        elif dealer_hand.get_value()>= player_hand.get_value()<= 17 or player_hand.get_value()>21:
            outcome ="dealer win"
            score -=1
        elif dealer_hand.get_value()< player_hand.get_value(): 
            outcome ="you win"
            score +=1
        in_play = False
            
        
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more

    # assign a message to outcome, update in_play and score

# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    #canvas.draw_text(text, point, font_size, font_color)
    #canvas.draw_text(text, point, font_size, font_color, font_face)
    global dealer_hand, player_hand
    player_hand.draw(canvas,[30,490] )
    if in_play:
        dealer_hand.draw(canvas,[30,190] )
        canvas.draw_text("Hit or stand?", (300, 450), 40, "Black")
    else:
        dealer_hand.draw(canvas,[30,190] )
    
    canvas.draw_text("Score = "+str(score), (400, 80), 40, "Black")
    canvas.draw_text("Blackjack", (50,80), 50, "Aqua")
    canvas.draw_text("Dealer", (30, 150), 40, "Black")
    canvas.draw_text(outcome, (220, 150), 40, "Black")
    canvas.draw_text("Player", (30, 450), 40, "Black")
    
    if not in_play:
        canvas.draw_text("New deal?", (300, 400), 40, "Black")


    

# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric