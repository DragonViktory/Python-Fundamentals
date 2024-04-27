my_dictionary = {'bread': 10, 'butter': 4, 'sugar': 9, 'jam': 12}
print(my_dictionary) #{'bread': 10, 'butter': 4, 'sugar': 9, 'jam': 12}
del my_dictionary["sugar"] #{'bread': 10, 'butter': 4, 'jam': 12}
print(my_dictionary)
del my_dictionary
print(my_dictionary) # ->NameError: name 'my_dictionary' is not defined