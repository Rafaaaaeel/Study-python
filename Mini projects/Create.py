import os 
path = 'C:\\Users\\rafae\\Documents\\Python\\Folders'
os.chdir(path) 

folders = ['folder 1','folder 2','folder 3'] 

#answer = input('Tell the folders names, separede by space ')
#folders = answer.split(' ') 

for i in folders : os.mkdir(i) 


