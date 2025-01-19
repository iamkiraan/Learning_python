# inbuilt date and times
import datetime as dt
x = dt.datetime.now()
print(x.year)
print(x.strftime("%A"))

# creating dates object
y = dt.datetime(2022,2,3)
print(y)
print(x.strftime("%B"))
