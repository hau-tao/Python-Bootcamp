# implementation of card game - Memory

import simplegui
import random
cards = range(0,8) + range (0,8)
exposed=[]
match=[]
index =[]
state = 0
count = 0




# helper function to initialize globals
def new_game():
    global state, count, exposed, label
    state = 0
    count = 0
    exposed =[]
    random.shuffle(cards) #shuffle cards
    label.set_text("Turns = "+str(count))
    for i in range(16):
        exposed.append(False) # initialize exposed to false
    print cards
    
   
     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global state, count, label
    global  exposed, first_card, second_card  
    if state == 0:
        exposed[pos[0]//50] =True
        first_card = pos[0]//50
        state =1
        print 'state', state
       
        
    elif state ==1:
        
        exposed[pos[0]//50] = True
        second_card = pos[0]//50
        if first_card != second_card:
            count = count +1
            label.set_text("Turns = "+str(count))
            print 'count'+ str(count)
            state = 2
            print 'state', state
        else:
            state = 1
        
    else:
        exposed[pos[0]//50] = True
       
       
        if pos[0]//50 != second_card and pos[0]//50 != first_card:
            if cards[first_card] !=cards[second_card]: 
                exposed[first_card] = False
                exposed[second_card] = False
                state =1
               
            elif cards[first_card] ==cards[second_card]:
                exposed[first_card] = True
                exposed[second_card] = True
                state =1
                
            first_card = pos[0]//50 
       
        
            
        
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global exposed , frame 
    for i in range(16):
        exposed.append(False)  
          
    for card_index in range(len(cards)):
        if exposed[card_index]== True:
            card_pos = 50 * card_index
            canvas.draw_text(str(cards[card_index]),(card_pos+10,50),50, 'White')
            canvas.draw_line((card_pos,0),(card_pos,100),1,'White')
            
            
        else:
            #card_pos = 50 * card_index
            #canvas.draw_line((card_pos,0),(card_pos,100),1,'Black')
             canvas.draw_polygon([(50*card_index, 0), (50*card_index+50, 0), (50*card_index + 50, 100), (50*card_index, 100)],1, "Black", "Green")


# create frame and add a button and labels

frame = simplegui.create_frame("Memory", 800, 100)
frame.set_canvas_background('Black')
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")



# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()

frame.start()


# Always remember to review the grading rubric