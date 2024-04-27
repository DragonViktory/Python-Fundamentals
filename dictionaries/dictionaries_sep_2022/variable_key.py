name = "name"
# def variable , kato key add variable
my_dictionary = {name: "Pesho", "age": 20, "key without value": ""}
print(my_dictionary[name])

name = "car"
my_dictionary = {name: "Pesho", "age": 20, "key without value": ""}
print(my_dictionary)

my_dictionary = {name: "Pesho", 1: 20, "key without value": ""}
print(my_dictionary)
# key - > int {'car': 'Pesho', 1: 20, 'key without value': ''}

my_dictionary = {name: "Pesho", 1.35: 20, "key without value": ""}
print(my_dictionary[1.35])
# key - > float # 20