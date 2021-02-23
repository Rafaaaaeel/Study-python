def square(x):
    return x * x

#print(square(3))

lambda_square = lambda x : x * x

#print(lambda_square(3))

double_mult = lambda x,y : 2 * x * y

#print(double_mult(2,3))

def name_and_alias(name,alias):
    return name.strip().title() + ':' + alias.strip().title()

name_and_alias1 = lambda name,alias:name.strip().title() + ':' + alias.strip().title()

print(name_and_alias(' john ClEEse  ','HECKLER'))
print(name_and_alias1(' john ClEEse  ','HECKLER'))

monty_python = ['John Marwood Cleese','Eric Idle','Michael Edward Palin','Terrence Vance Gilliam','Terry Graham Perry Jones', 'Graham Arthur Chapman']

monty_python.sort(key = lambda name : name.split(' '))
print(monty_python)
