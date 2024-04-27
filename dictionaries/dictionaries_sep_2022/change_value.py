my_dictionary = {"name": "Pesho", "age": 20, "key without value": ""}
print(my_dictionary["name"])
#Pesho
# my_dictionary["name"] = "Sasho"
# print(my_dictionary["name"])
# Sasho -> smenjame gi kato stoinosti na promenliva
my_dictionary["name1"] = my_dictionary["name"]
print(my_dictionary)
#{'name': 'Pesho', 'age': 20, 'key without value': '', 'name1': 'Pesho'}
# -> taka dobavjame kluch i stoinost in to the dictionary