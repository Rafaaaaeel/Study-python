a = 7
b = 3
print(a != b) # True
print(a == b) # False

#Another example

a = [3,7,42]
b = a
print(a == b) #True
print(a is b) #True
print(id(a), id(b)) # 2 and 2, but is because b recive a, but if you give a letter b the same list the answer change to 2 and 3 because is igual but not the same in memorie

print('o' in 'John') # True

# All number above 0 is True, 0 is False