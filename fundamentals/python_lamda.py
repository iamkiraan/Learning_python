# python lamda
x = lambda a,b,c,d : a+56
print(x(5,5,6,6))

# why to use lambda function
def calculate(x):
    return lambda a : a*x

value = calculate(8)
print(value(6))