#Excuse my English

"""Stopwatch: The Game"""
# The goal is to stop the watch at a whole second
# You can check it at http://www.codeskulptor.org/#user12_5YCMXQJyfG_5.py

# Import modules
import simplegui
import random

# define global variables
time = 0
formated_time = "00:00.0"
stop_clicks = 0
success_stop_clicks = 0
game_rules_result = "0/0"
last_stop_checker = False

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(time):
    """Formats the time (A:BC.D)"""
    
    global formated_time
    
    #Defien local variables 
    minutes = None
    seconds = None
    miliseconds = None
    
    #Reset timer every 1 hour
    time %= 60000
    
    #Separate the minutes from varible time using rounded-down devision
    minutes = time//1000
    
    #Adds "0" if minutes consist of only one didgit
    if minutes < 10:
       minutes = "0" + str(minutes)
    else:
        minutes = str(minutes)
    
    #Separate the seconds from varible time using rounded-down devision
    seconds = (time//10)%100
    
    #Adds "0" if seconds consist of only one didgit
    if seconds < 10:
        seconds = "0" + str(seconds)
    else:
        seconds = str(seconds)
    
    #Separate the miliseconds from varible time
    miliseconds = str(time%10)
    
    formated_time = minutes + ":" + seconds + "." + miliseconds

# define main logic of the game "Stopwatch: The Game" – called from stop_button()
def game_rules():
    """ Main game logic """
    
    # define variables
    global stop_clicks, success_stop_clicks, last_stop_checker, game_rules_result
    
    # Checks if STOP button is NOT clicked multiple consistent times and increment stop clicks counter +1
    if last_stop_checker == True:
        stop_clicks += 1
        # Checks if watch is stopped on a whole second
        if time%10 == 0:
            success_stop_clicks += 1
    
    # Formats result of the game in order to be passed to draw_handler
    game_rules_result = str(success_stop_clicks)+ "/"+ str(stop_clicks)
    
    # Change value to False in order to prevent miltiple consistent clicks
    last_stop_checker = False

# define event handlers for buttons; "Start", "Stop", "Reset"

def start_button():
    """ Defiens event handler Start Button """
    global last_stop_checker
    
    #Gives value True to global variable last_stop_checker to announce that a new count down has started
    last_stop_checker = True
    
    #Starts timer
    timer.start()

def stop_button():
    """ Defiens event handler Stop Button """
    
    #Stops timer
    timer.stop()
    
    #Calls main game logic
    game_rules()

    
def reset_button():
    """Resets all global variables"""
    global formated_time, time, stop_clicks, success_stops, game_rules_result
    
    time = 0
    stop_clicks = 0
    success_stops = 0
    game_rules_result = "0/0"
    formated_time = "00:00.0"

# define event handler for timer with 0.1 sec interval
def tick():
    """Counts the time unformated in miliseconds (incremetns global variable time)"""
    
    global time
    time += 1
    
    # Calls help that formats time in  (A:BC.D)
    format(time)
    
# define draw handler
def draw(canvas):
    canvas.draw_text(formated_time, [25, 100], 35, "Red")
    canvas.draw_text(game_rules_result, [25, 50], 25, "White")
    
# create frame
frame = simplegui.create_frame("Stopwatch: The Game", 300, 200)

# register event handlers
frame.add_button("Start", start_button, 100)
frame.add_button("Stop", stop_button, 100)
frame.add_button("Reset", reset_button, 100)
frame.set_draw_handler(draw)

#frame.set_draw_handler(draw)
timer = simplegui.create_timer(100, tick)

# start frame
frame.start()

# Please remember to review the grading rubric
