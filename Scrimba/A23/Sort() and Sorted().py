my_list = [5,1,3,7,2]
print(my_list, 'Original')

 

print(my_list, 'New')
my_dict = {'car':4,'dog':2,'add':3,'bee':1}

my_tuple = ('d','c','e','a','b')

my_string = 'python'

print(tuple(sorted(my_tuple)))


my_list = [1,5,-3,7,-2]
my_llist=[['car',4,65],['dog',2,30],['add',3,10],['bee',1,24]]
print(sorted(my_list, key = abs))

#Lambda function

print(sorted(my_llist, key = lambda item :item[2] ))


