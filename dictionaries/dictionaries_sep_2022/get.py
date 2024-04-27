# name = ["Pesho", "Nikolai", "Atanas"]
# my_dictionary = {"name": "Ivan", "age": 48, "city": "Sofia", "key without value": ""}
# print(my_dictionary["name"])
# print(my_dictionary["car"]) #-> Key error

name = ["Pesho", "Nikolai", "Atanas"]
my_dictionary = {"name": "Ivan", "age": 48, "city": "Sofia", "key without value": ""}
print(my_dictionary["name"])
# if "car" in my_dictionary.keys()
car = my_dictionary.get("car")
print(car)
# ->None
