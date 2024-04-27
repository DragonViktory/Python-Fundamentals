my_dictionary = {"name": ["Pesho", "Nikolai", "Atanas"], "age": 20, "key without value": ""}
my_dictionary["car"] = "Opel"
print(my_dictionary)
#{'name': ['Pesho', 'Nikolai', 'Atanas'], 'age': 20, 'key without value': '', 'car': 'Opel'}
#dobavja key + value nakraja
my_dictionary["car"].append("Opel")
#my_dictionary["car"].append("Opel")
#AttributeError: 'str' object has no attribute 'append'-> njama key

my_dictionary["car"] = []
my_dictionary["car"].append("Opel")
print(my_dictionary)
#my_dictionary["car"].append("Opel")
#AttributeError: 'str' object has no attribute 'append'

