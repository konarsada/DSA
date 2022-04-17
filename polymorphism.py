class Bird:
    def intro(self):
        print("There are many types of Birds")
    def flight(self):
        print("some fly, some dont")

class Sparrow(Bird):
    def flight(self):
        print("I fly")
class Ostrich(Bird):
    def flight(self):
        print("I dont")

obj_bird = Bird()
obj_spr = Sparrow()
obj_ost = Ostrich()
  
obj_bird.intro()
obj_bird.flight()
  
obj_spr.intro()
obj_spr.flight()
  
obj_ost.intro()
obj_ost.flight()