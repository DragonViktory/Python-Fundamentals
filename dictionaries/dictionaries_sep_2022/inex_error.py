# # my_dictionary = {"name": "Pesho", "age": 20, "city": "Sofia"}
# # print(my_dictionary[0])
# #KeyError: 0 -> ochakva da polychi key, ne moje da go dostupim po index. 07.dictionaries_lab njamat index
# my_dictionary = {"name": "Pesho", "age": 20, "city": "Sofia"}
# print(my_dictionary.keys()[0])
#TypeError: 'dict_keys' object is not subscriptable
name = ["Pesho", "Nikolai", "Atanas"]
my_dictionary = {"name": ["Pesho", "Nikolai", "Atanas"], "age": 20, "key without value": ""}
print(my_dictionary["name"][0])
#Pesho -> rabotja s 03.lists_basics_lab, tova e indeksa ot lista
