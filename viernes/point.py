class Point2d:
    def __init__(self, x, y):
        self._x=None
        self._y=None

        self.setX(x)
        self.setY(y)     

    def setX(self,x):
        if x<0:
            raise Exception("The X must be positive")
        else:
            self._x=x
    def setY(self,y):
        if y<0:
            raise Exception("The Y must be positive")
        else:
            self._y=y
    def getX(self):
        return self._x
    def getY(self):
        return self._y
    
    def translate(self, transX, transY):
        self._x=self.getX()+transX
        self._y=self.getY()+transY
    def getAsList(self):
        return [self.getX(), self.getY()]
    def print(self):
        print(self.getX(),self.getY())

class Point3D(Point2d):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self._z=None
        self.setZ(z)

    def setZ(self,z):
        if z<0:
            raise Exception("Z must be bigger than 0. And today is Friday")
        self._z=z
    def getZ(self):
        return self._z

    def translate(self, transX, transY, transZ):
        super().translate(transX,transY)
        self._z=self.getZ()+transZ
    def getAsList(self):
        return [self.getX(), self.getY(), self.getZ()]
    def print(self):
        print(self.getX(),self.getY(), self.getZ())   

if __name__=="__main__":
    p1=Point3D(1,1,1)

    p1.print()
    p1.translate(5,6,7)
    print(p1.getAsList())
    p1.print()

