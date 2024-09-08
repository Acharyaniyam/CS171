def main():
    sportsList = open('/Users/niyamacharya/Library/Mobile Documents/com~apple~TextEdit/Documents/sports.txt')
    sp = sportsList.read()
    print(sp)
    

def sportsList():
    sportsList = open('/Users/niyamacharya/Library/Mobile Documents/com~apple~TextEdit/Documents/sports.txt')
    for index in range(1, 11) : 
        sp = sportsList.readline () 
        print(str(index) + ". ", sp)

    sportsList = open('/Users/niyamacharya/Library/Mobile Documents/com~apple~TextEdit/Documents/sports.txt')
    for index in range(1, 11) :
        sp = sportsList.readline () 
        print( str ( index ) + ". ", sp.lstrip () )

    sportsList = open('/Users/niyamacharya/Library/Mobile Documents/com~apple~TextEdit/Documents/sports.txt')
    for index in range(1, 11) : 
          sp = sportsList.readline ()
          if len(sp) >= 8:
             print(sp.rstrip())
def main1() :
    lastName = input("Enter last name: ") 
    firstName = input("Enter first name: ") 
    studentID = input("Enter ID: ")
    inFile = open("studentInfo.txt", "a")
    inFile.write ("Name: " + firstName + " " + lastName)
    inFile.write ("\nStudentID: " + studentID ) 
    inFile.write ("\n") 
    inFile.close ()
    print("Done! Data is saved in file: studentInfo.txt")




import random

def integers():
    random.seed(28)
    for i in range(1,1001):
        integer = random.randint(1,25)
        textFile = open('randomNumbers.txt', 'a')
        textFile.write(str(integer) )
        textFile.write('\n')
        
    textFile.close()
    


def calculation():
    with open('randomNumbers.txt' , 'r') as inFile:
        numbers = [int(line.strip()) for line in inFile]

    average = sum(numbers) / len(numbers)
    maximum = max(numbers)
    minimum = min(numbers)
    print('The average of the random numbers is: ', average)
    print('The maximum of the random numbers is: ', maximum)
    print('The minimum of the random numbers is: ', minimum)

 
def isalpha():
    userInput = input("Enter a string that contains only letters: ")
    if userInput.isalpha () :
        print("Your string is valid.") 
    else :
        print("Your string does not contain all letters.")

def isdigit1():
    numString = input("Enter a number: ")
    if numString.isdigit () :
        num = int (numString) 
        print(num, "to the fourth power is", num ** 4)
    else :
        print("Your input is not a valid number.") 
        print("Program terminated!")

            
 
def txtfile1404():
    total_numbers = 0
    with open('/Users/niyamacharya/Documents/DREXEL SUMMER 2023/1404.txt', 'r') as inFile:
        for line in inFile:
            words = line.split()
            for word in words:
                if word.isdigit():
                    print(word)
                    total_numbers += 1
                    
    print('The total number of numbers found in the file is', total_numbers)
  
        
a = [17, 12, 10, 15, 0, 14, 13, 5, 0, 6]
a.desc()
        
        
        
        
        
        
        
        
        
        
        
        
        