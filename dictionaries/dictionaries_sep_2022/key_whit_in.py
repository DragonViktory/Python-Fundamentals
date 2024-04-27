my_dictionary = {"name": "Pesho", "age": 20, "key without value": ""}
print("car" in my_dictionary.keys())
#False
print("car" in my_dictionary)
#False
print("name" in my_dictionary.keys())
#True
print("name" in my_dictionary)
#True

print("Pesho" in my_dictionary.values())
#True
print("Pesho" in my_dictionary)
#False -> taka tursi po key, a "Pesho" ne e key

print("Pesho" in my_dictionary.items())
#False

my_dictionary = {"name": "Pesho", "age": 20, "key without value": ""}
print(my_dictionary.items())
print(my_dictionary.keys())
print(my_dictionary.values())
# dict_items([('name', 'Pesho'), ('age', 20), ('key without value', '')]) -> 03.lists_basics_lab whit tuple, ne obhojda vutreshnata my chast
# dict_keys(['name', 'age', 'key without value']) -> 03.lists_basics_lab
# dict_values(['Pesho', 20, '']) -> 03.lists_basics_lab
