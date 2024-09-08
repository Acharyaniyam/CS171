def hanoi3HardCoded(start, spare , end) : 
    print( start + " -> " + end)
    print( start + " -> " + spare)
    print( end + " -> " + spare)
    print( start + " -> " + end)
    print( spare + " -> " + start)
    print( spare + " -> " + end)
    print( start + " -> " + end)
    

def hanoi1CallingSimplerMethods ( start, end) :
    print( start + " -> " + end)

def hanoi2CallingSimplerMethods (start, spare, end):
    hanoi1CallingSimplerMethods (start, spare)
    print(start + " -> " + end)
    hanoi1CallingSimplerMethods (spare, end)
    
def hanoi3CallingSimplerMethods (start, spare, end):
    hanoi2CallingSimplerMethods (start, end, spare)
    print (start + " -> " + end)
    hanoi2CallingSimplerMethods (spare, start, end)

def hanoi4CallingSimplerMethods (start, spare, end):
    hanoi3CallingSimplerMethods (start, end, spare)
    print(start + ' -> ' + end)
    hanoi3CallingSimplerMethods (spare, start, end)
    
def hanoi (start, spare, end, n):
    if n == 1:
        print(start + " -> " + end)
    else:
        hanoi(start, end, spare, n - 1) 
        print(start + " -> " + end) 
        hanoi(spare, start, end, n - 1)

    
def hano_debug (start, spare, end, n):
    print("start = ", start, "spare = ", spare, "end = " , end)
    if n == 1:
        print(start + " -> " + end)
    else : 
        hanoi_debug (start, end, spare, n - 1) 
        print(start + " -> " + end) 
        hanoi_debug (spare, start, end, n - 1)


def hanoi_debug (start, spare, end, n):
    print ("start = ", start, "spare = ", spare, "end = ", end)
    if n == 1:
        print (start + " -> " + end)
    else: 
        hanoi_debug (start, end, spare, n) 
        print (start + " -> " + end) 
        hanoi_debug (spare, start, end, n)

import turtle

def square():
    
    turtle.penup()
    turtle.setpos(-100,-100)
    turtle.pendown()
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.penup()


def A(line):
    if line > 0:
        turtle.pendown()
        turtle.forward(line)
        turtle.right(90)
        turtle.forward(line)
        A(line - 5)

def B(line):
    turtle.right(90)
    if line > 5:
        turtle.pendown()
        turtle.forward(line)
        turtle.right(20)
        B(line - 15)
        turtle.left(40)
        B(line - 15)
        turtle.right(20)
        turtle.backward(line)
        turtle.penup()


def sierpinski(x, y, s):
    if s > 10:
        turtle.penup()
        turtle.setpos(x, y)
        turtle.pendown()
        for i in range(3):
            turtle.forward(s)
            turtle.left(120)
        
        sierpinski(x, y, s/2)
        sierpinski(x+s/2, y,s/2)
        sierpinski(x + s/4, y + (s * 3**(1/2)) / 4, s/2)
        
sierpinski(-100,-100,300)