# items = input().split()
# bakery = {}
# for index in range(0, len(items), 2): #-> zashoto sa po dvojki
#     bakery[items[index]] = int(items[index + 1]) # -> 10,4,9,12-> v output sa int,zatova int, suschtoto e kato bakery[key] = value #key = bread #value = 10 -> suzdavam rechnik s key i value
# print(bakery)

items = input().split()
bakery ={}
for element in items:
    bakery[element] = "Empty value"
    #taka vseki edin element ot 03.lists_basics_lab poluchava default value i vseki edin element poluchava key-element ot 03.lists_basics_lab:
    #{'bread': 'Empty value', '10': 'Empty value', 'butter': 'Empty value', '4': 'Empty value', 'sugar': 'Empty value', '9': 'Empty value', 'jam': 'Empty value', '12': 'Empty value'}
print(bakery)