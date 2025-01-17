# list = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(list[1])
# print(list[-1])
# print(list[2:5])
# if "apple" in list:
#     print(list[1]+ "is the furit")
# else:
#     print("not found")

# # changin the list
# list[1] = 'Kiran'
# print(list)
# list[1:3] = ["kiran ","acharya"]
# print(list)

# # adding values to the list
# list.append("avocardo")
# print(list)
# list.insert(2,"watermelon")
# print(list)

# # another list add garna ko lagi
# list2 = ['nepal','is','a']
# list.extend(list2)
# print(list)

# # removing items from list
# list.remove("apple")
# print(list)
# list.pop(1)
# print(list)
# del list
# print(list)


# loop in list
value = ['apple', 'kiran', 'cherry', 'orange', 'kiwi', 'melon', 'mango']
for a in value:
    print(a)

# new list comporehension
newList = []
for x in value:
    if "a" in x:
        newList.append(x)

print(newList)

# sorting elements in list
value.sort()
print(value)
value.sort(reverse=True)
print(value)

data = ["banana", "Orange", "Kiwi", "cherry"]
data.sort(key=str.lower)
print(data)

# copying list
some = data.copy()
print(some)

# joining the list
list1 = [1,2,3,4,5]
list2 = [5,6,7,8,9]
list3 = list1+list2
print(list3)
for x in list2:
    list1.append(x)
print(list1)
list1.extend(list2)
print(list1)

# tuples ko example
values = (True,False,True,False)
anothervalues  = {"kiran","acharya","nepal","country","lumbini"}
next = {"kiran","acharya","india","bowl"}
if(values[2]==True):
    print("the check is successful")
else:
    print("not successful")

print(len(values))

# sets ko example haru
l = anothervalues.union(next)
print(l)
p = anothervalues.intersection(next)
print(p)

