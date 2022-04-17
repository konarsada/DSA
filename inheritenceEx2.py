# multiple inheritence

class Person:
    def __init__(self, name):
        self.name = name
    
    def getName(self):
        return self.name
    
    def isPerson(self):
        return True

class Human:
    def __init__(self, sex):
        self.sex = sex
    
    def getSex(self):
        return self.sex
    
    def isHuman(self):
        return True

class Employee(Person, Human):
    def __init__(self, name, sex):
        Person.__init__(self, name)
        Human.__init__(self, sex)
    
    def isEmployee(self):
        return True

eric = Employee("Eric-Abidal", "Male")

print(
        eric.isEmployee(),
        eric.isHuman(),
        eric.isPerson(),
        eric.getName(),
        eric.getSex()
    )