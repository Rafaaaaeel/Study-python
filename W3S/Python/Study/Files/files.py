import re

open_file = open('txt.txt', 'r')

read_file = open_file.read()


x = re.sub('\n', '-', read_file)

x = re.split('-', read_file)

print(x)

