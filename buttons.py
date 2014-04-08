# starting point for calculator
import simplegui

# initialize globals
store = 12
operand = 3

# define functions that manipulate store and operand
def output():
    print "Store =", store
    print "Operand =", operand
    print ""

def swap():
    global store, operand
    store, operand = operand, store
    output()

def add():
    global store, operand
    store = store + operand
    output()

def sub():
    global store, operand
    store = store - operand
    output()

frame = simplegui.create_frame("Caculate", 200, 200)
frame.add_button("Print", output, 100)
frame.add_button("swap", swap, 100)
frame.add_button("Add", add, 100)
frame.add_button("Sub", sub, 100)

frame.start()
