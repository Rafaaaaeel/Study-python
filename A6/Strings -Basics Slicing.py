msg='welcome to it\'s Python 101: Strings'
print(msg+msg)
#Or
print(msg*2)
#Or
print(msg,msg)

print(msg.upper()) #WELCOME TO PYTHON 101: STRINGS

print(msg.lower()) # welcome to python 101: strings

print(msg.capitalize())  # Welcome to python 101: strings

print(msg.title()) # Welcome To It'S Python 101: Strings

print(len(msg)) # 30 count the number of letters

print(msg.count('o')) # numbers of letter 'o' in the phrase

#slicing

print(msg[0]) # letter 'w'
print(msg[5]) # letter 'm'
print(msg[-1]) # s the last letter

print(msg[:7]) # anwser is only 'welcome'