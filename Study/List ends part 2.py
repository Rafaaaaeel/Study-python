x = [5,10,15,20,25]
y = [2,32,125,200,10]
z = []

def r(l):
    for i in l: 
        if i == l[-1] or i == l[0] : z.append(i)
    return [z]

print(r(y))