i = input("numbers")
l = i.split()

a, b, c = l

def m(x,y,z):
    if int(x) > int(y) and int(x) > int(z):
        print(x)
    elif int(y) > int(x) and int(y) > int(z):
        print(y)
    else:
        print(z)

print(m(a,b,c))