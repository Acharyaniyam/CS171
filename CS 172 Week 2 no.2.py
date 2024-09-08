from point import Point
from random import randint

if __name__ == '__main__':
    howMany = int(input('how many points do you want to create? '))
    myPoints = []
    
    for count in range(0, howmMany):
        x = randint(0, 50)
        y = randint(0, 50)
        p = Point(x, y)
        myPoints.append(p)
        
    print('here are all your points: ')
    for point in myPoints:
        pStetr = point.strPoint()
        print(pStr)