def calculatePoints(word):
    word = word.lower()
    letter_points = {'a': 1, 'e': 1, 'i': 1, 'o': 1, 'u': 1, 'l': 1, 'n': 1, 's': 1, 't': 1, 'r': 1,
        'd': 2, 'g': 2,
        'b': 3, 'c': 3, 'm': 3, 'p': 3,
        'f': 4, 'h': 4, 'v': 4, 'w': 4, 'y': 4,
        'k': 5,
        'j': 8, 'x': 8,
        'q': 10, 'z': 10}
    sum =0
    for i in word:
        sum += letter_points.get(i, 0)

    return sum

print(calculatePoints('Python'))

def maxPointsWord(words):
    max_points = 0
    max_word = ''
    for i in words:
        points = calculatePoints(i)
        if points > max_points:
            max_points = points
            max_word = i
    return max_word

print(maxPointsWord(['Python', 'Java', 'Perl', 'Ruby', 'Honoluluz']))

def findMinMax(numbers):
    max_number = numbers[0]
    min_number = numbers[0]
    for i in numbers:
        if i > max_number:
            max_number = i
        if i < min_number:
            min_number = i 
    required_tuple = (min_number, max_number)
    return required_tuple

print(findMinMax([55, 1, 23, 64, 77, 99, 99]))

def isValidDate(month, day, year):
    if  (1 <= month <= 12):
      days_in_month = {'January': 31, 'February': 28, 'March': 31, 'April': 30, 'May': 31, 'June': 30,
                      'July': 31, 'August': 31, 'September': 30, 'October': 31, 'November': 30, 'December': 31}
      month_number = {1:'January', 2:'February', 3:'March', 4:'April', 5:'May', 6:'June',
                      7:'July', 8:'August', 9:'September', 10:'October', 11:'November', 12:'December'}
      month_inputted = month_number[month]
      days_in_inputted_month = days_in_month[month_inputted]
      if (year > 0) and (1 <= day <= days_in_inputted_month):
        return True
      else:
        return False
    else:
      return False


print(isValidDate(99, -1, -2015))

def calculateTotalMealCost(mealCost, taxRate = 0, tipPercentage = 0):
  total_cost = mealCost + mealCost * taxRate / 100 + mealCost * tipPercentage / 100
  return total_cost

print(calculateTotalMealCost(120.75, 8, 20))
    

        
        



