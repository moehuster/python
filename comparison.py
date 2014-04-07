# Comparison Operators

a = 7 > 3
print a

x = 8
y = 5
b = x >= y
print b

c = "Hello" == 'Hello'
print c

d = 20.6 <= 18.3
print d

print (a and b) or (c and (not d))

def greet(friend, money):
    if friend and (money > 20):
        print "Hi!"
        money = money - 20
    elif friend:
        print "Hello"
    else:
        print "Ha ha"
        money = money + 10
    return money

money = 15

money = greet(True, money)
print "Money:", money
print ""

money = greet(False, money)
print "Money:", money
print ""

money = greet(True, money)
print "Money:", money
print ""
