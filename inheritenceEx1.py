class Person:
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber
    
    def display(self):
        print("My name is", self.name,
                  "IdNumber", self.idnumber)
    
class Employee(Person):
    def __init__(self, name, idnumber, salary, post):
        self.salary = salary
        self.post = post
        
        # super().__init__(name, idnumber)
        Person.__init__(self, name, idnumber)
    
    def details(self):
        print("My name is",self.name,
              "IdNumber", self.idnumber,
              "Post", self.post,
              "Salary", self.salary)

a = Employee("Rahul", 13, 25000, "PAT")

a.display()
a.details()