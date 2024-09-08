def convertToBase(number, base):
    if number < base:
        return str(number)
    
    quotient = number // base
    remainder = number % base
    return convertToBase(quotient, base) + str(remainder)

def main():
    while True:
        try:
            number = int(input("Enter an integer between 1 and 1000: "))
            if not (1 <= number <= 1000):
                print("Error: you entered a value out of range. Try again.")
                continue
            
            while True:
                try:
                    base = int(input("Enter an integer between 2 and 9: "))
                    if 2 <= base <= 9:
                        break
                    else:
                        print("Error: you entered a value out of range. Try again.")
                except ValueError:
                    print("Invalid input: an integer value was expected. Try again.")
                    
            
            result = convertToBase(number, base)
            print(f"The equivalent of {number} in base {base} is {result}")
            
            choice = input("Do you have another number to convert (Y / N)? ").lower()
            if choice != 'y':
                print("OK, Good-bye!")
                break
        except ValueError:
            print("Invalid input: an integer value was expected. Try again.")

if __name__ == "__main__":
    main()
