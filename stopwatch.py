# template for "Stopwatch: The Game"

import simplegui

# define global variables
cur_time = 0    # Current time
bingo = 0       # Successful stops
total = 0       # Total stops

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    fraction = t % 10
    seconds = t / 10 % 60
    minutes = t / 600
    return "%d:%02d.%d" % (minutes, seconds, fraction)

# define event handlers for buttons; "Start", "Stop", "Reset"
def start_btn_handler():
    timer.start()

def stop_btn_handler():
    global cur_time, bingo, total
    if (timer.is_running()):
        total += 1
        if (cur_time % 10 == 0):
            bingo += 1
        timer.stop()

def reset_btn_handler():
    global cur_time, bingo, total
    cur_time = bingo = total = 0
    timer.stop()

# define event handler for timer with 0.1 sec interval
def tick():
    global cur_time
    cur_time += 1
    if (cur_time == 6000):
        timer.stop()

# define draw handler
def draw(canvas):
    canvas.draw_text(format(cur_time), [50, 90], 36, "White")
    canvas.draw_text(str(bingo)+"/"+str(total), [150, 20], 20, "Red")

# create frame
frame = simplegui.create_frame("Stopwatch", 200, 140)

# register event handlers
timer = simplegui.create_timer(100, tick)
frame.set_draw_handler(draw)
frame.add_button("Start", start_btn_handler, 80)
frame.add_button("Stop", stop_btn_handler, 80)
frame.add_button("Reset", reset_btn_handler, 80)

# start frame
frame.start()

# Please remember to review the grading rubric
