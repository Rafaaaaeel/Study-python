names = ['john ClEEse','Eric IDLE','michael']
names1 = ['graHam chapman', 'TERRY', 'terry jones']

names.extend(names1)

while True:
    names.append(input('add name of friend do you want to invite: '))

    answer = input('Do you want add more names? [Y/N] ')
    if answer == 'N':
        break

    print(names)

for i in names:
    print(i.title())

# Teacher solution


names = ['john ClEEse','Eric IDLE','michael']
names1 = ['graHam chapman', 'TERRY', 'terry jones']
msg = 'You are invited to the party on saturday.'
names.extend(names1)
#names = names + names1
for index in range(2):
    names.append(input('Enter a new name: '))

for name in names:
    msg1 = f'{name.title()}! {msg}'
    print(msg1)

