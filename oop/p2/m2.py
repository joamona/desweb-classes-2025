
import sys, os
#sys.path.append('c:\\desweb\\oop')

BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

print(BASE_DIR)
sys.path.append(BASE_DIR)

from p1 import m1


m1.f1()

def f2():
    print('I am f2')

if __name__=="__main__":
    print("I am p2.m2")
    print(__file__)