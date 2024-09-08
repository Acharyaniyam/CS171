# Programmer = Niyam Acharya
# Program date = July 18, 2023
# Program Description = A program that helps create user names for employees in a company.

# define the function below this line
def generateUserName(first_name, middle_name, last_name, birth_year, birth_month):
    
    user_name = first_name[0].lower() + middle_name[0].lower() + last_name[0:3].lower() + str(birth_month) + str(birth_year)[2:5]
    return user_name

# the main script
if __name__ == "__main__":
    # main script code goes below this line. Keep the same indentation level as this line.
    first_name = input('Enter your first name: ')
    middle_name = input('Enter your middle name: ')
    last_name = input('Enter your last name: ')
    birth_month = input('Enter your birth month: ')
    birth_year = input('Enter your birth year: ')
    
    months = {'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6, 'July': 7, 'August': 8, 'September': 9, 'October': 10, 'November': 11, 'December': 12}
    month_display = months.get(birth_month)
    
    
    print('Your user name is: ' + generateUserName(first_name, middle_name, last_name, int(birth_year), month_display ))
    