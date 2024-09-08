# Your header comment goes here
# Programmer = Niyam Acharya
# Program date = Aug 1, 2023
# Program description = A program that helps you calculate the number of days required for you to reach the required distance for the event, if you increase your distance each day by 10% from the previous day.


# Define required function under this line
def daysToDistance(initialDistance, goalDistance):
    days_required = 1
    while initialDistance < goalDistance:
        initialDistance *= 1.1
        days_required += 1
    return days_required

# The main script
if __name__ == "__main__":
    while True:
        try:
            initialDistance = int(input("Enter initial distance in miles:\n"))
            if initialDistance <= 0:
                print("Error: enter a value greater than zero")
                goalDistance =int(input())
        except ValueError:
            print('Error: enter an integer value')

    while True:
        try:
            goalDistance = int(input('Enter goal distance in miles:\n'))
            if goalDistance <= 0:
                print("Error: enter a value greater than zero")
                goalDistance =int(input())
            
        except ValueError:
            print('Error: enter an integer value')

    days_required = daysToDistance(initialDistance, goalDistance)
    print('You will need {} day(s) to achieve your goal'.format(days_required))

