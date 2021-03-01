#! python

def Main():

class Powers(object):
    def __init__(self, square, cube):
        self._square = square
        self._cube = cube
     
    def getSquare(self):
        return self._square ** 2
    
    def setSquare(self, value):
        self._square = value
      
    square = property(getSquare, setSquare)
     
    def getCube(self):
        return self._cube ** 3
     
    cube = property(getCube)

class Powers2(object):
    class DescSqure(object):
        def __get__(self, instance, owner):
            return instance._square ** 2
        
        def __set__(self, instance, value):
            instance._square = value
    
    class DescCube(object):
        def __get__(self, instance, owner):
            return instance._cube ** 3
    
    square = DescSquare()
    cube = DescCube()
    
    def __init__(self, square, cube):
        self._square = square
        self._cube = cube


if __name__ == '__main__':
    Main()
