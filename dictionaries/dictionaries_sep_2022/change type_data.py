my_dictionary = {"name": ["Pesho", "Nikolai", "Atanas"], "age": 20, "key without value": ""}
print(my_dictionary["name"])
my_dictionary["name"] = "Pesho"
print(my_dictionary["name"])
my_dictionary["name"] = 5
print(my_dictionary["name"] )
#['Pesho', 'Nikolai', 'Atanas']
#Pesho -> str
#5 -> int
# promenjam tipa danni v lista i tjahnata stojnist
# ako promenjam key, to smenjam negovata stojnost, a ne dobavjam now key,
# ako opitam vtori pat da my dam stojnost, to prosto prezapisva negovata stojnost
