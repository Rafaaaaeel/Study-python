import os # 1
path = 'C:\\Users\\rafae\\Documents\\Python\\Folders' # 1
os.chdir(path) # 1

folders = ['folder 1','folder 2','folder 3'] # 1

#answer = input('Tell the folders names, separede by space ')
#folders = answer.split(' ') 

for i in folders: # 3
    os.mkdir(i) # 3


