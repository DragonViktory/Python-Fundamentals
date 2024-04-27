my_dictionary = {"names": ["Pesho", "Nikolai", "Atanas"], "age": 20, "key without value": ""}
print(my_dictionary["names"])
# ['Pesho', 'Nikolai', 'Atanas'] -> 03.lists_basics_lab in dict

my_dictionary = {"names": {"Pesho": "ot Sofia", "Nikolai" : "ot Plovdiv"}, "age": 20, "key without value": ""}
print(my_dictionary["names"])
#{'Pesho': 'ot Sofia', 'Nikolai': 'ot Plovdiv'}
#-> dict in dickt - nested dickt

my_dictionary = {"names": "Pesho", "age": 20, "key without value": ""}
my_dictionary["name"] = "Pesho"
my_dictionary["name"] = "Nikolay"
print(my_dictionary)
# -> taka samo promenjam stojnost sreshy kluch
