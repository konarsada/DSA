class Dog:
    # class variable
    animal = "Dog"
    
    # constructor
    def __init__(self, breed):
        self.breed = breed
    
    # instance variable
    def setColor(self, color):
        self.color = color
    
    def __del__(self):
        print("deleted")

roger = Dog("Pug")
roger.setColor("Brown")

print(roger.breed, roger.color)

del roger