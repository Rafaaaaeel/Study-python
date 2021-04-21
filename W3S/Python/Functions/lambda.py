x = lambda a : a + 10

#print(x(10))

z = lambda a, b : a + b

#print(z(2,2))

def dupl(n):
    return lambda a : a * n

d = dupl(3)

print(d(10))
