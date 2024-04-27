my_dictionary = {'a': 100, 'b': 97, 'c': 50}
print(sorted(my_dictionary.items(), key=lambda key_value: (key_value[1], key_value[0])))
# [('c', 50), ('b', 97), ('a', 100)]
# samo sorted - ['a', 'b', 'c'] -> print key
# s lambda po key i value
# from collections import OrderedDict
