f = open('test.txt', 'a')

#f.write('this is the new content in the document')
f.close()

f = open('test.txt', 'r')
print(f.read())