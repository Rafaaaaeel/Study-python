for num in range(2,8,2):
    print(num)
print('-----------------------')
for names in ['rafael','sasha','noah']:
    print(names)

friends = ['rafael','sasha','noah']
print('-----------------------')
for index in range(len(friends)):
    print(friends[index])

print('-----------------------')
for friend in friends:
    if friend == 'sasha':
        print('Found ' + friend + '!')
        break
    print(friend)
print('-----------------------')
for friend in friends:
    if friend == 'sasha':
        print('Found ' + friend + '!')
        continue
    print(friend)
print('-----------------------')
for friend in friends:
    for number in [1,2,3]:
        print(friend, number)

print("For Loop done!")

