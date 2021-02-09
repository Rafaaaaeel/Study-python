friends = {'John','Michael','Terry','Eric','Graham'}
my_friends = {'Reg','Loretta','Colin','John','Graham'}
cars =['900','420','V70','911','996','V90','911','911','S','328','900']


#Sets - Exercise

#1. Check if ‘Eric’ and ‘John’ exist in friends
print('Eric' in friends and 'John' in friends)

#2. combine or add the two sets 
print(friends.union(my_friends))
print(friends | my_friends) # Create a new list removing the copy 

#3. Find names that are in both sets
print(friends.intersection(my_friends))
print(friends & my_friends) # Return only the duplicate values in both

#4. find names that are only in friends
print(friends.difference(my_friends))
print(friends - my_friends) # Return the value duplicate only 

#5. Show only the names who only appear in one of the lists
print(my_friends.symmetric_difference(friends))
print(my_friends ^ friends) # Create a new list with de value duplicate

#6. Create a new cars-list without duplicates
cars_no_dupl = list(set(cars))
print(cars_no_dupl)

