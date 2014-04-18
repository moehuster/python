# "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import random

# initialize global variables used in your code
num_range = 100
guess_remain = 7
guess_number = 0

# helper function to start and restart the game
def new_game():
    global guess_remain, guess_number
    if (num_range == 100):
        guess_remain = 7
    else:
        guess_remain = 10
    guess_number = random.randrange(0, num_range)
    print "New game, Range is from 0 to", num_range
    print "Number of remaining guesses is", guess_remain
    print ""

# define event handlers for control panel
def range100():
    # button that changes range to range [0,100) and restarts
    global num_range, guess_remain
    num_range = 100
    guess_remain = 7
    new_game()

def range1000():
    # button that changes range to range [0,1000) and restarts
    global num_range, guess_remain
    num_range = 1000
    guess_remain = 10
    new_game()

def input_guess(guess):
    # main game logic goes here
    global guess_remain
    guess_remain = guess_remain - 1
    print "Guess was", guess
    print "Number of remaining guesses is", guess_remain

    if (int(guess) < guess_number):
        print "Higher!\n"
    elif (int(guess) > guess_number):
        print "Lower!\n"
    else:
        print "Correct!\n"
        new_game()
    if (guess_remain == 0):
        print "The number is", guess_number
        print "Game over!\n"
        new_game()

# create frame
f = simplegui.create_frame("Guess the number", 200, 200)

# register event handlers for control elements
f.add_button("Range is [0, 100)", range100, 200)
f.add_button("Range is [0, 1000)", range1000, 200)
f.add_input("Enter a guess", input_guess, 200)

# call new_game and start frame
new_game()

# always remember to check your completed program against the grading rubric
