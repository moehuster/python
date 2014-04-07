# Remainder - modular arithmetic

# systematically restrict computation to a range
# long division - divide by a number, we get a quoitent plus remainder
# quotient is interget division //, the remainder is % (docs)

# problem - get the ones digit of a number
num = 49
tens = num // 10
ones = num % 10
print tens,ones
print tens * 10 + ones

# clock arithmetic - 24 hour clocks
hour = 20
shift = 8
print (hour + shift) % 24

# application - screen wraparound
# spaceship from week seven
width = 800
position = 2
move  = -5
position = (position + move) % width
print position

# Data conversion operations

# convert an integer into string - str
# convert an hour into 24-hour format "%03:00", always print zero
hour = 3
ones = hour % 10
tens = hour // 10
print tens, ones, ":00"
print str(tens) + str(ones) + ":00"

# convert a string into numbers using int and float

# Python modules - extra functions implemented outside basic
