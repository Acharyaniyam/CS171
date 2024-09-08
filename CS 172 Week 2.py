from math import sqrt


class Point:
    
    #static / class attribute
    __count = 0
    #construction: initiative the data member
    def __init__(self, x = 0 , y = 0):
        self.__x = x
        self.__y = y
        # we need to update the static data member every time a point is created
        Point.__count += 1
        
        #getters, inspectors, accersors
    
    def getX(self):
        return self.__x
    
    def getY(self):
        return self.__y
    
    def getCoordinates(self):
        return (self.__x, self.__y)
    
    # setters, mutators = changes the data members
    def setX(self, x):
        self.__x = x
        
    def setY(self, y):
        self.__y = y

    def setPoint(self, x, y):
        self.__x = x
        self.__y = y
    
    def reset(self):
        self.setPoint(0, 0)
        
    #other useful methods
    # helper method to help display point objects
    def strPoint(self):
        pStr = '(' + str(self.__x) + ',' + str(self.__y) + ')'
        return pStr
    def distance(self, other):
        return sqrt( ((self.getX() - other.getX()) ** 2) + ((self.getY() - other.getY()) ** 2) )

    #static / class methods
    @staticmethod
    def getPointCount():
        return Point.__count