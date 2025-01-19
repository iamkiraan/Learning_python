try:
    print(x)
except NameError:
    print("variable is not defined")
except:
    print("an exception occurred")


try:
    print("x")
except : 
    print("error occured")
else:
    print("nothing happened")

    # finally
try:
    print(x)
except:
    print("error occured")
finally:
    print("try except finished")

# working with file

try:
    f = open("demon.txt")
    try:
        f.write("hello there")
    except:
        print("cannot write something went wrong")
    finally:
        f.close()
except:
    print("something went wrong")

# raising exception

x = -1
if x<0:
    raise Exception("sorry")

# type error
x = "kiran"
if not type(x) is int:
    raise TypeError("only integers are allowed")


