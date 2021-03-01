def greeting(name,age=0):# Def is = Define
    born = int(2020 - age) 
    if age <= 21:
        print(f'Hello {name}! you are {age} you born in {born}, you can`t not drink')
    else:
        print(f'Hello {name}! you are {age} you born in {born}, you can drink')
    
     

greeting("Rafael",21)