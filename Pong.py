# Implementation of classic arcade game Pong
# You can check it at http://www.codeskulptor.org/#user13_zpRBcS80BP_2.py


import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2

ball_vel = [0, 0]
right = random.randint(0, 1)
left_player_score = 0
right_player_score = 0


left_paddle_pos = 0
right_paddle_pos = 0


paddle1_vel = 0
paddle2_vel = 0
left_paddle_vel = 0
right_paddle_vel = 0

# helper function that spawns a ball by updating the 
# ball's position vector and velocity vector
# if right is True, the ball's velocity is upper right, else upper left
def ball_init(right):
    """"""
    global ball_pos, ball_vel # these are vectors stored as lists
    
    # Spowns(respowns) ball at the center of canvas
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    
    # Adds randomization to the start velocity
    # Defines direction of the ball
    if right:
        ball_vel[0] = random.randrange(1, 5)
        ball_vel[1] = -random.randrange(1, 5)
    else:
        ball_vel[0] = -random.randrange(1, 5)
        ball_vel[1] = -random.randrange(1, 5)

# define event handlers

def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are floats
    global left_player_score, right_player_score  # these are ints
    
    ball_init(right)

def draw(c):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel, left_player_score, right_player_score, left_paddle_pos, left_paddle_vel, right_paddle_pos, right_paddle_vel 
    
    # update paddle's vertical position, keep paddle on the screen
   
        
    # draw mid line and gutters
    c.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    c.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    c.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    
    
    # makes the ball collides with and bounces off of the top and bottom walls
    if ball_pos[1] > (HEIGHT-BALL_RADIUS) or ball_pos[1] < BALL_RADIUS:
        ball_vel[1] =  -ball_vel[1]
    
    # tests whether the ball collides with the left and right gutters
    # updates players score
    if ball_pos[0] < (BALL_RADIUS + PAD_WIDTH):
        ball_init(1)
        left_player_score += 1
        
    elif ball_pos[0] > (WIDTH - BALL_RADIUS - PAD_WIDTH):
        ball_init(0)
        right_player_score += 1
    
    # calculate ball position
    ball_pos[0] = ball_pos[0] + ball_vel[0]
    ball_pos[1] = ball_pos[1] + ball_vel[1]
    
    # calculate paddles position
    # checks if paddles are in visible area
    left_paddle_pos = left_paddle_pos + left_paddle_vel
    right_paddle_pos = right_paddle_pos + right_paddle_vel
    
    if left_paddle_pos < 0 or left_paddle_pos > (HEIGHT - PAD_HEIGHT):
        left_paddle_vel = 0
    
    if right_paddle_pos < 0 or right_paddle_pos > (HEIGHT - PAD_HEIGHT):
        right_paddle_vel = 0
    
    # draw paddles
    c.draw_line((HALF_PAD_WIDTH, left_paddle_pos), (HALF_PAD_WIDTH, left_paddle_pos + PAD_HEIGHT), PAD_WIDTH, "White")
    c.draw_line((600 - HALF_PAD_WIDTH, right_paddle_pos), (600 - HALF_PAD_WIDTH, right_paddle_pos + PAD_HEIGHT), PAD_WIDTH, "White")
    
    # update ball
    
                
    # draw ball and scores
    c.draw_text(str(left_player_score), [WIDTH / 2 -50, 50], 35, "Red")
    c.draw_text(str(right_player_score), [WIDTH / 2 +30, 50], 35, "Red")
    c.draw_circle(ball_pos, BALL_RADIUS, 1, "White", "White")
    
def keydown(key):
    global paddle1_vel, paddle2_vel, left_paddle_vel, right_paddle_vel
       
    if key == simplegui.KEY_MAP['w']:
        left_paddle_vel = -5
        
    elif key == simplegui.KEY_MAP['s']:
        left_paddle_vel = 5

    if key == simplegui.KEY_MAP['up']:
        right_paddle_vel = -5
    
    elif key == simplegui.KEY_MAP['down']:
        right_paddle_vel = 5
        
   
def keyup(key):
    global paddle1_vel, paddle2_vel, left_paddle_vel, right_paddle_vel
    left_paddle_vel = 0
    right_paddle_vel = 0


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)


# start frame
frame.start()
new_game()
print left_paddle_pos