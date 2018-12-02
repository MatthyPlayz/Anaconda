from random import randint, uniform
import math
class Acda:
    zero = 0
    infish = math.factorial(99999)
    def Floorrandom(a, b):
        return randint(a, b)
    def Strrandom(stringlist):
        li = stringlist;
        rand = randint(0, len(li))
        return li[rand]
    def Unfloorrandom(a, b):
        return uniform(a, b)
    def Undefined():
        return None
    
