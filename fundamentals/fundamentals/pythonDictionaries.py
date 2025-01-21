values = {
    "name" : "kiran acharya",
    "age": "23",
    "address" : "kalikot",
    "contact" : 9865445343,
    "hobby" : ["football","cricket","swimming"]
    
}
print(values)
print(values["name"])
print(len(values))
term = values["hobby"]
print(term[1])
x = values.get("hobby")
print(x)
# values haru add garnalaii
values["tone"] = "dark"
print(values)
# check if the key and value exists

if "tone" in values :
    print("yes! tone exixts")

# removing the items from the dict

values.pop("tone")
print(values)


# nested dictionaries

# child = {
#     "child1"={
#         "name" : "name1",
#         "age" : 22
#     },
#     "child2" = {
#         "name" : "name2",
#         "age" : 24
#     }
# }

