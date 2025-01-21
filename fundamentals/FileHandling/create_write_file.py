f = open("test.txt","a")
userInput = input("")
f.write(userInput)
f.close()

f = open("test.txt")
print(f.read())