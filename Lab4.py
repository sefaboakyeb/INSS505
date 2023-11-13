#count 0 to 10
for s in range(0,11):
    print(s)

#count 1 to 10
for t in range(1,11):
    print(t)

#count 1 to 10 with increment of +2
for eachpass in range(1,10,2):
    print(eachpass,end="")

#import math
import math
radius=float(input("enter the radius for a circle:"))
math.pi
if radius>0:
    area = ((math.pi * radius ** 2))
    print("the area of a circle with radius",radius, "is", area)
else:
    print("the radius entered is not greater than 0. area of circle cannot be calculated")
#logic for area of rectangle
length=float(input("enter the length of a rectangle"))
width=float(input("enter the width of a rectangle"))
if length > 0 and width > 0:
    area= length * width
    print("the area of rectangle with length",length,"and width",width, "is", area)
else:
    print("enter width and/or length greater than 0")





