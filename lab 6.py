#take input from user
while True:
    num = int(input("enter number > 0:"))
    if num >0:
        break
    else:
        print("invalid. please enter a number > 0")
if num % 2 == 0:
    print(num, "is an even number")
else:
    print(num, "is an odd number")
if num == 1:
    print(num, "is not a prime number")

    #check if number is a prime number or not

#if given number is greater than 1
#define a main variable
main = False

if num == 1:
    print(num, "is not a prime number")
elif num > 1:
    #check for factors
    for m in range (2, num):
        if (num % 1) == 0:
            #if factor is found, set main to True
            main = True
            #break out of loop
            break

    #check if main is true
    if main:
        print(num, "is not a prime number")
    else:
        print(num, "is a prime number")