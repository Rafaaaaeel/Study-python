#It’s...not really an adventure game...#Ver 1.0
#Your village is being attacked by 'a germanic tribe' and you need to run to the stores and get the right things to save your village, and probably some good looking girl or boy you want to marry. All prices in gold pieces excl. VAT... chop chop!! ze germanz are coming!
#The code should allow you to get 1 thing from each store and each item you get should be removed from the store inventory, then do same for next store...
# one way to buy by typing the key 'newt' in an input box...or something
# at end you should print the 'items' you have taken..in this version you don't have to pay for stuff or add it up
#ver 1.2 add ability to exit a store without buying and go to next by typing 'exit', and to exit if a nonexistant item is bought(typed)
#Add purse with 1000 gold pieces and payment for the items during or at end of code and show a message about total cost and how much gold you have left
#ver 1.4 random bug fix, ' browser compatability', refactoring code... basically being lazy ..stop scrolling TikTok/Facebook! ;-)
#Ver 1.5 print inventory before and after purchases as one department_store of stuff(combine inventories from all stores into one...pretend Big Biz bought all the local stores, and want constant reporting for inventory management...)
# as in all games there is a special way to do this that actually makes money and solves the problem...can you find 'them'? Do you know why? May require knowledge of actual python 'lore'

#create stores

freelancers = {'name':'freelancing Shop','brian': 70, 'black knight':20, 'biccus diccus':100, 'grim reaper':500, 'minstrel':200}
antiques = {'name':'Antique Shop','french castle':400, 'wooden grail':3, 'scythe':150, 'catapult':75, 'german joke':5}
pet_shop = {'name':'Pet Shop','blue parrot':10, 'white rabbit':5, 'newt': 2}


# Anwser

player_inventory = []
player_wallet = 0

while True:
        
    # Veryfication for print the items on player inventory
    if len(player_inventory) > 0: 
        for inventory in player_inventory:
            print('---------Your items---------')
            print(inventory)
            print('------------Cash------------')
            print(f"You have in your wallet ${player_wallet}")
            print('----------------------------')
    else:
        player_wallet = 1000
        print(f"You have in you wallet ${player_wallet}")
        


    place_to_go = input('where do yo want to go? : ')

    if place_to_go == 'f' or 'F':
        while True:
            
            if len(player_inventory) > 0:
                break
            print('-----freelancers Store-----')
            for num, items in enumerate(freelancers):
                print(num,"-", items)
    
            while True:
                choose = input('What do you want choose for the list? [exit] to leave ')

                if choose == 'exit':
                    break

                if choose == "0":
                    print('Sorry this is not an item try again')
                elif choose == "1":
                    player_wallet -= 70
                    freelancers.pop('brian')
                    player_inventory.append('brian')
                    break
                elif choose == "2":
                    player_wallet -= 20
                    freelancers.pop('black knight')
                    player_inventory.append('black knight')
                    break
                elif choose == "3":
                    print(player_wallet - 100)
                    freelancers.pop('biccus diccus')
                    player_inventory.append('biccus diccus')
                    break
                elif choose == "4":
                    player_wallet -= 500
                    freelancers.pop('grim reaper')
                    player_inventory.append('grim reaper')
                    break
                elif choose == "5":
                    player_wallet -= 200
                    freelancers.pop('minstrel')
                    player_inventory.append('minstrel')
                    break

            if choose == 'exit':
                break
              
            
    if place_to_go == 'p':
        print('-----antiques Store-----')

        for num,items in enumerate(antiques):
            print(num,"-",items)
        
        while True:
            choose = input('What do you want choose for the list? [exit] to leave ')

            if choose == 'exit':
                break

            if choose == "0":
                print('Sorry this is not an item try again')
            elif choose == "1":
                player_wallet -= 400
                antiques.pop('french castle')
                player_inventory.append('french castle')
                break
            elif choose == "2":
                player_wallet -= 30
                antiques.pop('wooden grail')
                player_inventory.append('wooden grail')
                break
            elif choose == "3":
                print(player_wallet - 150)
                antiques.pop('scythe')
                player_inventory.append('scythe')
                break
            elif choose == "4":
                player_wallet -= 35
                antiques.pop('catapult')
                player_inventory.append('catapult')
                break
            elif choose == "5":
                player_wallet -= 50
                antiques.pop('german joke')
                player_inventory.append('german joke')
                break

        if choose == 'exit':
            break

    