import os

def scan_folders(initial_folder, folder = '', level = 0):
    path = os.path.join(initial_folder, folder)

    if not os.path.isdir(path):
        return

    files = os.listdir(os.path.join(initial_folder, folder))

    for file in files:
        print('\t' * level, '>',file)
        scan_folders(path, file, level + 1)

path = 'C:/Users/rafae/Documents'

scan_folders(path)