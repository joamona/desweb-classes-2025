class Point2D:
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

class Point3D(Point2D):
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
        print("Cambio")  


class Po2d:
    def __init__(self,l: list[Point2D]):
        self.l:list[Point2D]=l
    def sumXY(self):
        
        return [self._sumCoordinate('_x'), self._sumCoordinate('_y')]
    def _sumCoordinate(self,propertyName):
        sum=0
        for p in self.l:
            sum+=getattr(p,propertyName)
        return sum
    
class Po3D(Po2d):
    def __init__(self, l:list[Point3D]):
        super().__init__(l)
        self.pp:list[Point3D]=None
    def sumXYZ(self):
        l2=self.sumXY()
        l2.append(self._sumCoordinate('_z'))
        return l2




def sumaNPrimerosNumeros(n):
    a=1
    b=2
    c=a+b
    sum=0
    for i in range(n):
        i=i+1
        print(i)
        sum = sum + i
        print(sum)

def getMinOfList(l):
    min=l[0]
    for e in l:
        if e<min:
            min = e
    return min

if __name__=="__main__":
    """p1=Point3D(1,1,1)

    p1.print()
    p1.translate(5,6,7)
    print(p1.getAsList())
    p1.print()
    """
    #sumaNPrimerosNumeros(5)


    p1=Point3D(10,10,10)
    p2=Point3D(20,30,40)
    l=[p1,p2]

    po3=Po3D(l)
    print(po3.sumXYZ())
    print(po3._sumCoordinate('_x'))
