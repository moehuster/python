# computes the area of triangle
def triangle_area(base, height):
    area = (1.0/2) * base * height
    return area

#test
a1 = triangle_area(3, 8)
print a1

a2 = triangle_area(14, 2)
print a2

# converts fahrenheit to celsius
def fahrenheit2celsius(fahrenheit):
    celsius = (5.0/9) * (fahrenheit - 32)
    return celsius

#test
c1 = fahrenheit2celsius(22)
c2 = fahrenheit2celsius(212)
print c1, c2

# converts fahrenheit to kelvin
def fahrenheit2kelvin(fahrenheit):
    celsius = fahrenheit2celsius(fahrenheit)
    kelvin = celsius + 273.15
    return kelvin

#test
k1 = fahrenheit2kelvin(32)
k2 = fahrenheit2kelvin(213)
print k1, k2

# print hello, world!
def hello():
    print "hello, world!"

#test
h = hello()
print h
