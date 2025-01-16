list = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(list[1])
print(list[-1])
print(list[2:5])
if "apple" in list:
    print(list[1]+ "is the furit")
else:
    print("not found")

# changin the list
list[1] = 'Kiran'
print(list)
list[1:3] = ["kiran ","acharya"]
print(list)

# adding values to the list
list.append("avocardo")
print(list)
list.insert(2,"watermelon")
print(list)

# another list add garna ko lagi
list2 = ['nepal','is','a']
list.extend(list2)
print(list)