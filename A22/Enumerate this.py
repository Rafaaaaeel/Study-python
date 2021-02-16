print('python101 - Enumerate')
friends = ['Brian', 'Judith', 'Reg', 'Loretta', 'Colin']

i = 1

#for friend in friends:
    #print(i, friend)
    #i += 1

for num, friend in enumerate(friends,1):
    print(num, friend)