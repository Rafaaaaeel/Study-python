import re

txt = 'The rain in Spain'

x = re.search("^The.*Spain$", txt)

if x:
    print('Yes')
else:
    print('No')


x = re.findall("ai", txt)
print(x)

x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start())

x = re.split("\s", txt)
print(x)

x = re.split("\s", txt, 1)
print(x)

x = re.sub("\s", "-", txt)
print(x)

x = re.search("ai", txt)
print(x)