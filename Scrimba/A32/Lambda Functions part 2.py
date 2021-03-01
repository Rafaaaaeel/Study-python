def func(n):
    return lambda a : a * n

dowbler = func(2)

#print(dowbler(3))

def price_calc(start,hour_rate):
    return lambda hours : start + hour_rate * hours

walkin_cost = price_calc(10,30)
premium_cost = price_calc(1,25)

print(walkin_cost(2))
print(premium_cost(2))
print(price_calc(1,25)(2))

print((lambda a,b,c: a+b+c)(2,3,4))
print((lambda a,b,c=2: a+b+c)(2,3))
print((lambda *args: sum(args))(2,3,4,49))