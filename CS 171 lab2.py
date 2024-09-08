print(abs(4.5) )
print(pow(5, 3) )
print(pow(49, 0.5) )
print( int ('34') )
print(round(-5.6) )



print(10*5-2*3%4)
print(10-5%4+3*2)
print(10+5//4-3**2)


import math 
x = 4.7 
y = 5.3 
z = -4.8 
a = -3.2
print(math.ceil(x)) 
print(math.ceil(y)) 
print(math.ceil(z)) 
print(math.ceil(a)) 
print(math.floor(x)) 
print(math.floor(y)) 
print(math.floor(z)) 

def printMessage ():
    print("Welcome to Python.") 
    print("Learn the power of functions!")

#Function Definition 
def main() :
    print("Hello Programmer!")
#Function Call
    printMessage ()

    printMessage ()   
#Function Call 
main()


import math

def calculateArea (radius):
    area = math.pi * radius ** 2 
    print("A circle of Radius %d has area %.2f"  %(radius, area))

def main() :
 
    calculateArea(6)
    
#### Call to main #### 
main()


def frog():
    print('   @..@')
    print(' ( ---- )')
    print('( > _ _ < )')
    print('^ ^ __ ^ ^')


def main2():
    for i in range(1,5):
        print('Frog', i)
        frog()

main2()

import random

def getMessage(userNum, randNum):
    if userNum == randNum:
        print('You picked the same number as the computer!')
    elif userNum > randNum:
        print('Your number is higher than the computer’s number.')
    else:
        print('Your number is smaller than the computer’s number.')
        
def main() :
    userNum = int (input("Enter a number between 1 and 5: ") ) 
    while userNum > 5 or userNum < 1:
        userNum = int (input("Invalid number. Enter a number between 1 and 5: ") )
    randNum = random.randint (1, 5) 
    print("Computer number:", randNum) 
    print("User number:", userNum) 
    getMessage(userNum, randNum) 
    
    ##Call Main 
main()

def  print_feet_inch_short(num_feet, num_inches):
    print(f'{num_feet}\', {num_inches}\"')
    
''' Your solution goes here '''

user_feet = int(input())
user_inches = int(input())

print_feet_inch_short(user_feet, user_inches) # Will be run with (5, 8), then (4, 11)