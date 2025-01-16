# x = "Sally"
# x = 4
# print(x)
#multiple variables at a time
x,y,z = 2,3,4
# print(x,y,z) 

x = y = z = "Orange"
# print(x[0])
# print(y[1])
# print(z[2])

# unpacking the collection
fruits = ["orange","apple","banana"]
x = y = z = fruits
# print(x,y,z)

# global variables ko kura
x = 6
def myFunc():
    x = 9
    print(x+5)
myFunc()
print(x)

def func():
    x =3
    x = 'fantastic'
func()
print(x)



