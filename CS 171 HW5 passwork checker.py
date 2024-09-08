# YOUR HEADER COMMENT GOES HERE
#Programmer = Niyam Acharya
# Program date = Aug 1, 2023
# Program description = A program to simulate a password checker that let us know whether or not a password is valid


# Define required function under this line
def checkPassword(password):
    if (len(password) < 12):
        return False
    if ' ' in password:
        return False
    if not any(i.isupper() for i in password):
        return False
    if not any(i.islower() for i in password):
        return False
    if not any(i.isdigit() for i in password):
        return False
    special_character = ['!','@','#','$','%','^','&','*','(',')','_','+','[',']','{','}','|',';',':',',','.','<','>','?','/','`','~','-']
    if not any(i in special_character for i in password):
        return False
    
    return True 


# The main script
if __name__ == "__main__":
    # code for the main script goes under this line, all indented
    
    while True:
        password = str(input('Enter a password: '))
        if checkPassword(password) == True:
            print('{} is valid and meets all the criteria'.format(password))
            break
        else:
            print('{} fails to meet the criteria. Try again.'.format(password))
            
