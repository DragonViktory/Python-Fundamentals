class Animal:
    species = "humans"
# class Atribut, ako ne go nameri v inizializatora tursi v class atributi
    def __init__(self, name):
        self.name = name


test_obj = Animal("Gosho")
print(test_obj.name)
print(test_obj.species)
