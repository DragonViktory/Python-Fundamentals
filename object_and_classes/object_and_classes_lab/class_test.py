class Test:
    def __init__(self, num_a, num_b):
        self.num_a = num_a
        self.num_b = num_b

    def sum_numbers(self):
        return self.num_a + self.num_b


obj = Test(5, 10)
print(obj.sum_numbers())

