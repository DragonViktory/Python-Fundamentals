items = input().split() #['bread', '10', 'butter', '4', 'sugar', '9', 'jam', '12'] -> chetno chislo
bakery = {}
for index in range(0, len(items), 2): #-> zashoto sa po dvojki
    key = items[index] # -> bread, butter,sugar, jam
    value = int(items[index + 1]) # -> 10,4,9,12-> v output sa int,zatova int
    bakery[key] = value #key = bread #value = 10 -> suzdavam rechnik s key i value
print(bakery)