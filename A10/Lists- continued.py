friends = ['John','Michael','Terry','Eric','Graham']
cars = [911,130,328,535,740,308]
print(friends)

friends.sort()

friends.sort(reverse = true) 

min_car =  min(cars)

max_car = max(cars)

print (max_car)

friends.append('Rafael')

friends.insert(1,'Leticia')

friends[1] = 'Sasha'

friends.extend(cars)

friends.remove('John')

friends.pop(2) # O item 'Removido' continua na memoria do compudador

friends.clear() # A lista fica limpa para ser adivionada novos valores a ela

del friends #Isso ira remover de vez a lista

new_friends = friends[:]
new_friends_1 = friends.copy()
new_friends_2 = list(friends)

print(new_friends)
print(new_friends_1)
print(new_friends_2)