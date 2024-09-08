# Programmer = Niyam Acharya
# Program date = July 18, 2023
# Program Description = Program for a fast food restaurant that allows its customers to create their own version of a happy meal


# define the function below this line
def calculateMealCost(main, side, drink):
    cost = 0
    cost = main.get(main_choice.upper()) + side.get(side_choice.upper()) + drink.get(drink_choice.upper())
    total_cost = cost + cost * 0.08
    return total_cost

# the main script
if __name__ == "__main__":
    # main script code goes below this line. Keep the same indentation level as this line.
    main = {'BURGER': 8.36, 'CHICKEN SANDWICH': 7.19, 'VEGGIE WRAP': 7.25, 'VEGGIE BURGER': 9.61}
    side = {'FRIES': 2.55, 'SALAD': 4.19, 'FRUIT': 4.15, 'CHIPS': 2.09}
    drink = {'SODA': 2.29, 'WATER': 2.59, 'TEA': 2.69, 'LEMONADE': 3.15}
    
    print('Build your own meal menu')
    print('Entrees: burger | chicken sandwich | veggie wrap | veggie burger')
    print('Sides: fries | salad | fruit | chips ')
    print('Drinks: soda | water | tea | lemonade \n')
    
    main_choice = input('Choose your entree: ')
    side_choice = input('Choose your side dish: ')
    drink_choice = input('Choose your drink: ')
    
    print('The total cost of your meal is: ${:.2f}'.format(calculateMealCost(main, side, drink)))


    
    
    
    