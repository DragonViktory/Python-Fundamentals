my_dictionary = {'bread': 10, 'butter': 4, 'sugar': 9, 'jam': 12}
print(my_dictionary.items())
for items in my_dictionary.items():
    print(items)
# ('bread', 10)
# ('butter', 4)
# ('sugar', 9)
# ('jam', 12)
# print(f"Key is {key}, value is {value}")
print(my_dictionary.items())
for key, value in my_dictionary.items():
    print(f"Key is {key}, value is {value}")
   