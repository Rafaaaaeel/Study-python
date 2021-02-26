import random, string

for i in range(5):
    #print(random.uniform(1,6))
    #print(random.randint(1,6))
    #print(random.randrange(1,100,2))
    pass
friends_list =  ['John', 'Eric', 'Michael', 'Terry', 'Graham']
#print(random.choice(friends_list))
#print(random.sample(friends_list,3))
random.shuffle(friends_list)
#print(friends_list)

smallcaps = 'abcdefghijklmnopqrstuvwxyz'
largecaps = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
digits = '0123456789'
letters_numbers = string.ascii_letters + string.digits

word = ''

for i in range(9):
    word += random.choice(letters_numbers)

word2 = random.choices(friends_list, k=2)   

print(word2)
