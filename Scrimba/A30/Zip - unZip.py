nums = '1234' 
letters = ['a','b','c','d','e']
#names =['John','Eric','Michael','Graham','Joe']
combo = dict(zip(nums,letters))
print(combo)

# Dict 
print('----------------')

keys = 'this parrot is deceased'
values = 'denna papegojan är avliden'
keys = keys.split()
values = values.split()
print(keys,values)
en_sv_dict = dict(zip(keys,values))
print('----------------')
print(en_sv_dict)
new_dict = {key:value for key,value in zip(keys,values)}
print('----------------')
print(new_dict)
en,sv = list(en_sv_dict.keys()),list(en_sv_dict.values())
print('----------------')
print(en,sv)
en1,sv1 = zip(*en_sv_dict.items())
print('----------------')
print(en1,sv1)
print('----------------')
a = "1234"
b = ['Rafael','Sasha','Noah']

c = dict(zip(a,b))

print(c)

x,z = zip(*c.items())

print(x)
print(z)