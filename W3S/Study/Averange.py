a = {
        'Rafael':24,
        'leticia':15,
        'Sasha':21,
        'Noah':15,
        'Wagner':20
    }

b = sum(a.values()) / len(a)

print('average:',b)

print('--------------')

for j,i in a.items():
    if  i < b : print(j)
        