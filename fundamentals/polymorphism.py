# polymorphism in python
# same method name with multiple classes


class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    def move(self):
        print("drive carefully")

class Boat:
    def __init__(self,brand,model):
        self.model = model
        self.brand = brand
    def move(self):
        print("sail carefully")

class areoplane:
    def __init__(self,model,brand):
        self.model = model
        self.brand = brand
    
    def move(self):
        print("fly carefully")

car1 = Car("toyota","first")
boat = Boat("dont know","hello")
areo = areoplane("fly emirates","88480")

for x in (car1,boat,areo):
    x.move()
        