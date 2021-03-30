# Imports external modules
import random
import time

# Objects creators
class Person:
    def __init__(self,name,damage,health):
        self.name = name
        self.damage = damage
        self.health = health

class weapon:
    def __init__(self,name,damage):
        self.name = name
        self.damage = damage

# Function for choose the weapon
def choose_weapon(item):
    if item == "Glock":
        return weapons_list["Glock"].damage
    if item == "Ak-47":
        return weapons_list["Ak-47"].damage
    if item == "Katana":
        return weapons_list["Katana"].damage

# Objects dict
weapons_list = {
    "Glock": weapon("Glock",20),
    "Ak-47": weapon("Ak-47",70),
    "Katana": weapon("Katana",45)
}

character_list = {
    "Hero" : Person("Will", random.randint(1,5), 100),
    "villain" : Person("Jhon", random.randint(1,5), 100)
}

# List to can pass an argument in "choose_weapon" function using the random module
character_start = [x for x in character_list.keys()]
character_weapon = [x for x in weapons_list.keys()]


# THE GAME RUNNING
while True:
    who_is_the_first = random.choice(character_start)

    if character_list["Hero"].health >= 100 and character_list["villain"].health >= 100: 
        #count up
        for i in range(1,4): 
            time.sleep(1) 
            print(i)
            if i == 3 : print("Fight")

    # Giving the weapons
    character_list["Hero"].damage = choose_weapon(random.choice(character_weapon))
    character_list["villain"].damage = choose_weapon(random.choice(character_weapon))

    # if for not let both die in at the same time 
    if character_list["Hero"].damage == character_list["villain"].damage: 
        continue 
    else: 
        time.sleep(1)
        print(f"Hero life is: {character_list['Hero'].health}")
        print(f"Villain life is: {character_list['villain'].health}")
            
    if who_is_the_first == "Hero":
        if character_list["Hero"].health <= 0 or character_list["villain"].health <= 0: 
            break
        else:
            print("Hero is going to attack \n")
            time.sleep(1)
            character_list['villain'].health -= character_list['Hero'].damage
            print(f"Villain life is: {character_list['villain'].health}")
            time.sleep(1)
            print("Villain is going to attack \n")
            character_list['Hero'].health -= character_list['villain'].damage
            print(f"Hero life is: {character_list['Hero'].health}")
        
        

    if who_is_the_first == "villain":
        if character_list["Hero"].health <= 0 or character_list["villain"].health <= 0: 
            break
        else:
            time.sleep(1)
            print("Villain is going to attack \n")
            time.sleep(1)
            character_list['Hero'].health -= character_list['villain'].damage
            print(f"Hero life is: {character_list['Hero'].health}")
            time.sleep(1)
            print("Hero is going to attack \n")
            character_list['villain'].health -= character_list['Hero'].damage
            time.sleep(1)
            print(f"Villain life is: {character_list['villain'].health}")

        


