#!/usr/bin/python3


print("Standard quad formual ax^2 +bx +c")
a = float(input("Please enter (a) value: "))
b = float(input("Please enter (b) value: "))
c = float( input("please enter (c) value:"))

square = ((b**2)-4*a*c)**0.5 #calculates discriminate
test = b**2 / (4 * a * c)    #compares b^2 to 4ac to determine which way to calculate formula


#test to see if b^2 is much larger
if test > 10.0 and b > 0:
    r1 = (2*c) / (-b - square)
    r2 =  (-b - (square)/ (2*a))
    print("tripped 1")

#tests to see if b^2 is much larger and negative
if test > 10.0 and b < 0:
    r1 = (-b + square) / (2 * a)
    r2 = (2*c) / (-b + square)
    print("tripped 2")
#standard way to calculate quad_formula
if test < 10.0:
    r1 = (-b + square) / (2*a)
    r2 = (-b -square) / (2*a)
    print("tripped standard")



print(" first root: ",r1)
print("\n second root: ", r2)
