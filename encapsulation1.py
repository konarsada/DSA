class Base:
    def __init__(self):
        # private property
        self._a = 10
        
        # protected property
        self.__b = 20
    
    def checkBoth(self):
        print(self._a)
        print(self.__b)

class Derived(Base):
    def getPrivate(self):
        self._a = 30
        print(self._a)
    
    def getProtected(self):
        print(self.__b)

a = Derived()

a.checkBoth()

# accessing private property outside
# class is bad practice / theoretically
# not possible
print(a._a)

# print(a.__b)

a.getPrivate()

# a.getProtected()