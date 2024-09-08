multiple_of_5 = int(input('Enter a multiple of 5 between 1 to 100: '))
if (multiple_of_5  % 5 == 0) and (1 < multiple_of_5 < 100) :
    print('The number is valid')
else:
    print('The number is invalid.')
    