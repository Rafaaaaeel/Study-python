import os 
path = 'C:\\Users\\rafae\\Documents\\Python\\test'
os.chdir(path) 

folders = ['folder 1','folder 2','folder 3'] 

#answer = input('Tell the folders names, separede by space ')
#folders = answer.split(' ') 

for i in folders : 
    if os.path.exists(i):
        print(f'File does exist {i}')
        continue
    os.mkdir(i)
    print(f'Create: {i}')


