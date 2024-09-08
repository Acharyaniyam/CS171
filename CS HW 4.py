# Programmer = Niyam Acharya
# Program date = July 26, 2023
# Program description =  A program that asks the user to enter their birth year and tell them their zodiac animal and their traits.


# define required functions below this line
def findZodiacAnimal(year):
    zodiac = {0 : 'Monkey', 1 : 'Rooster', 2 : 'Dog', 3 :  'Pig', 4 : 'Rat', 5 : 'Ox', 6 : 'Tiger', 7 : 'Rabbit', 8 : 'Dragon', 9 : 'Snake', 10 : 'Horse', 11 : 'Goat'}
    remainder = year % 12
    animal = zodiac[remainder]
    return animal
    
def getTraits(animal):
    traits = {'monkey' : 'sharp, smart, curiosity', 'rooster' : 'observant, hardworking, courageous', 'rat': 'quick-witted, resourceful, versatile, kind','dog' : 'loyal, honest, prudent', 'pig' : 'compassionate, generous, diligent', 'ox' : 'diligent, dependable, strong, determined', 'tiger' : 'brave, confident, competitive', 'rabbit' : 'quiet, elegant, kind, responsible', 'dragon' : 'confident, intelligent, enthusiastic', 'horse' : 'animated, active, energetic', 'goat' :'calm, gentle, sympathetic', 'snake': 'enigmatic, intelligent, wise'}
    
    animal_traits = traits[animal.lower()]
    
    return animal_traits

# the main script  
if __name__ == "__main__":
 
 try:
      year = int(input('Enter your birth year: '))
      if year > 0:
          print('You were born on the year of the', findZodiacAnimal(year))
          print('You are', getTraits(findZodiacAnimal(year)))
      else:
          print('Invalid year')
 except ValueError:
          print('Invalid input: you did not enter a year')
     