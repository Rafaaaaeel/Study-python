import random
import time

class Person:
    def __init__(self,name,damage,health):
        self.name = name
        self.damage = damage
        self.health = health

class Special:
    def __init__(self,name,damage):
        self.name = name
        self.damage = damage


Special_list{
    "Glock": Special("Glock",20),
    "Ak-47": Special("Ak-47",70),
}

character_hero = Person("Will", random.randint(1,5), 100)
character_ant_hero = Person("Jhon", random.randint(1,5), 100)



while True:
    pass



