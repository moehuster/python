### String Processing

# String literals
s1 = "Rixner's funny"
s2 = 'Warren wears nice ties!'
s3 = ' T-shirts!'

#print s1, s2
#print s3

# Combining strings
s4 = "Warren" + ' and ' + "Rixner" + ' are nuts!'
#print s4

# Characters and slices
print s1[-1]
print len(s1)
print s1[0:6] + s2[6:]
print s2[:13] + s1[9:] + s3

# Converting strings
s5 = str(375)
print s5
i1 = int(s5[1:])
print i1 + 30

# convert xx.yy to xx dollars and yy cents
def convert(val):
    dollars = int(val)
    cents = int(100*(val-dollars))
    return str(dollars) + " dollars and " + str(cents) + " cents"

# Test
print (convert(11.23))
print (convert(11.20))
