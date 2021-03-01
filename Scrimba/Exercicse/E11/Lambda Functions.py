print('Lambdas Exercise')


#Code below OK
f = lambda x : x + 5

print(f(2))

#------------------------------------#

#Code below OK
strip_spaces_l = lambda stri : ' '.join(stri.split(' '))

print(strip_spaces_l('Monty Pythons Flying Circus')) 


#------------------------------------#


list_a = [1,2,3,4]
list_b = [3,4,5,6,7]

#Code below Ok
join_list_no_duplicate_l = lambda list_a,lista_b : list(set(list_a + list_b))

print(join_list_no_duplicate_l(list_a,list_b))





#Complete the function so it returns a function
def create_quad_func(a,b,c):
    '''return function f(x) = ax^2 + bx + c'''
    return lambda x: a*x**2 + b*x + c
f = create_quad_func(2,4,6)
g = create_quad_func(1,2,3)
print(f(2))
print(g(2))








signups = ['MPF104', 'MPF20', 'MPF2', 'MPF17', 'MPF3', 'MPF45']
#print(sorted(signups)) # Lexicographic sort
#write sorting by integer
print(sorted(signups,key = lambda id:int(id[3:]))) # Integer sort




class Player:
   def __init__(self, name, score):
       self.name = name
       self.score =  score

Eric = Player('Eric', 116700)
John = Player('John', 24327)
Terry = Player('Terry', 150000)
player_list = [Eric, John, Terry]


#Exercise: Sort this by score using lambda!
#write code here
player_list.sort(key = lambda playyer: playyer.score)
print([player.name for player in player_list])

