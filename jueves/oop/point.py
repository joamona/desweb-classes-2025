API_URL='http://localhost:8000'

class Point:
    def __init__(self, x, y):
        self._x=None
        self._y=None

        self.setX(x)
        self.setY(y)     
        
    def setX(self,x):
        if x < 0:
            raise Exception("The x must be positive")
        self._x=x
    def setY(self,y):
        if y < 0:
            raise Exception("The y must be positive") 
        self._y=y

    def getX(self):
        return self._x
    def getY(self):
        return self._y
    
    def translate(self, transX, transY):
        a="Local variable"
        self._x=self.x+transX
        self._y=self.y+transY

    def print(self):
        print(a)
        print(self.getX(), self.getY())

if __name__=="__main__":
    p1=Point(-10,10)
    p1.translate(5,8)
    p1.getY()
    p1.setY(80)
    p1.print()
