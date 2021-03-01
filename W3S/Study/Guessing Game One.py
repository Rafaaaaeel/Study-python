import random

random_number = random.randint(1,9)

print(random_number)
print('====================================================================================================')
print('Guessing game, you choose a random number between 1 and 9, and i tell if your anwser is close or far and right ok <3')
print('====================================================================================================')

guess = 0
count = 0

while guess != random_number and guess != 'exit':
    guess = int(input('Number: '))

    if guess == 'exit':
        break
    
    guess = int(guess)
    count += 1

    if guess < random_number:
        print('too low')
    elif guess > random_number:
        print('Too high')
    else:
        print(f"yes the number is {random_number}")
