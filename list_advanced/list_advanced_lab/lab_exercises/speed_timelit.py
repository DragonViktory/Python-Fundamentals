import timeit

a = timeit.timeit(stmt='''lst = []
for n in range(10000):
    lst.append(n)''', number=10000)

b = timeit.timeit(stmt='lst = [n for n in range(10000)]', number=10000)

print(a)
print(b)