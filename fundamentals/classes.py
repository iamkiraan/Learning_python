class MyClass:
    x = 5
    # yeta chaii Myclass ko object create hunxa
p1 = MyClass()
print(p1.x)

# init function ko example

class ClassMy:
    def __init__(self,age,name):
        self.name = name
        self.age = age

p1 = ClassMy(23,"kiran acharya")
# print(p1.name)
# print(p1.age)

class ClassM:
    def __init__(self,age,name):
        self.name = name
        self.age = age
    def __str__(self):
        return f"{self.name} ({self.age})"
p1 = ClassM(23,"kiran")
print(p1)

# object method 

class ClasM:
    def __init__(self,age,name):
        self.name = name
        self.age = age
    def myFunc(self):
        print("hello my name is" + self.name)
p1 = ClasM(23,"kiran")
p1.myFunc()
