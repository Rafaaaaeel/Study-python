import random
import time

class Person:
    def __init__(self,name,damage,health):
        self.name = name
        self.damage = damage
        self.health = health

class weapon:
    def __init__(self,name,damage):
        self.name = name
        self.damage = damage


weapons_list = {
    "Glock": weapon("Glock",20),
    "Ak-47": weapon("Ak-47",70),
    "Katana": weapon("Katana",45)
}

character_list = {
    "Hero" : Person("Will", random.randint(1,5), 100),
    "villain" : Person("Jhon", random.randint(1,5), 100)
}

character_start = [x for x in character_list.keys()]

weapon_choice = input(f"Choice a weapon {weapons_list.keys()}").capitalize()

def chosee_weapon(*item):
    if item == "Glock":
        return int(weapons_list["Glock"].damage)
    if item == "Ak-47":
        return weapons_list["Ak-47"].damage
    if item == "Katana":
        return weapons_list["Katana"].damage

character_weapon = [x for x in weapons_list.keys()]

weapon_choice = chosee_weapon(weapon_choice)
print(weapon_choice)


#while True:
#
 #   how_is_gonna_be_work = random.choice(character_start)
  #  
   # if how_is_gonna_be_work == "Hero":
    #    if weapon_choice != "":
     #       character_list["Hero"].damage = weapon_choice
#
 #           another_weapon = str(random.choice(character_weapon))
  #          #print(another_weapon)
   #         character_list["villain"].damage = chosee_weapon(another_weapon)
    #        #print(another_weapon)
     #       #print(character_list["villain"].damage)    
#
#
 #      character_list['villain'].health -= character_list['Hero'].damage
  #      
  #      time.sleep(10)
#
 #       character_list['Hero'].health = character_list['villain'].damage
#
 #       break

