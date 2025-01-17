# if you do not know how manyt args need to be passed you can use *

def myFunc(*name):
    print(name)
myFunc("kiran","acharya")

# default parameter

def known(name = "kiran"):
    print(name)

known()
known("acharya")
known("hello")


# list haru pass garna laii
def value(fruits):
    for x in fruits:
        print(x)

values = ["orange","apple","maggo"]
value(values)


# retruning values
def returning(x):
    return x*5

print(returning(4))
print(returning(8))

# recursion ko example


def recursion(k):
    if(k==1 or k ==0):
        return 1
    else :
        return k * recursion(k-1)

value = recursion(6)
print(value)