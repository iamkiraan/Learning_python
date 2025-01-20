f = open("hello.txt","w")
f.write("file to delete")

import os

if os.path.exists("kiran.txt"):
    os.remove("kiran.txt")
else:
    print("file doesnot exixts")

if os.path.exists("hello.txt"):
    os.remove("hello.txt")
else:
    pass