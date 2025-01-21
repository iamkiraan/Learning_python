myTuple = ("orange","apple","mago")
myit = iter(myTuple)
print(next(myit))
print(next(myit))
print(next(myit))

# string can also be iterated
myString = "Exmaple"
myit = iter(myString)
print(next(myit))
print(next(myit))
print(next(myit))

# create an iterator

class Myclass :
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a+=1
            return x
        else :
            raise StopIteration

myclass = Myclass()
myitr = iter(myclass)
for y in myitr:
    print(y)