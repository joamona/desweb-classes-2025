class Point:
    def __init__(self, x:float, y:float):
        self.x=float(x)
        self.y=float(y)
    def printCoordinates(self):
        print([self.x, self.y])
        
class Po:
    def __init__(self, lll):
        self.aaa:list[Point]=lll

    def sumXY(self):
        sumx=0
        sumy=0
        for p in self.aaa:
            sumx += p.x 
            sumy += p.y
        return [sumx, sumy]
    
    def geocenterXY(self):
        l=self.sumXY()
        n=len(self.aaa)
        return [l[0]/n, l[1]/n]
    
    def anOther(self):
        pass
    def translate(self, dx, dy):
        l=[]
        for p in self.aaa:
            p1=Point(x=p.x+dx, y=p.y+dy)
            l.append(p1)
        return l

    def translate2(self, dx, dy):
        for p in self.aaa:
            p.x+=dx
            p.y+=dy
        return self.aaa

    def printAaaa(self, l:list[Point]=None):
        if l is None:
            self._printListaPuntos(self.aaa)
        else:
            self._printListaPuntos(l)

    def _printListaPuntos(self, listaPuntos:list[Point]):
        print("--- Point list ---")
        for p in listaPuntos:
            p.printCoordinates()

if __name__=="__main__":
    l=[Point('1',1), Point(2,5)]
    po=Po(l)
    print(po.sumXY())
    print(po.geocenterXY())
    l2=po.translate(5,5)
    po.printAaaa(l2)
    po.translate2(5,5)
    po.printAaaa()
