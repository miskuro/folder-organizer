import os
import shutil
import time


def type(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.05)


extensionTypes = []

directory = os.getcwd()

type("enter the names of the folders u wanna create:  \n (and separate using commas(,) and no spaces): \n")
folderInput = input(">>>")
foldersToMake = folderInput.split(',')

type("now enter the extension (.txt/.png...) to each of them in the same order  \n (and separate using commas(,) and no spaces): \n")
extensionInput = input(">>>")
extensionTypes = extensionInput.split(',')



for folder in foldersToMake:
    folder_path = os.path.join(directory, folder)
    try:
        os.makedirs(folder_path, exist_ok=True)
        print(f"newFolder: {folder_path}")
    except Exception as e:
        print(f"Error creating folder: {e}")


for file in os.listdir(directory):
    file_path = os.path.join(directory, file)  
    if os.path.isfile(file_path):
        _, file_extension = os.path.splitext(file)

        for i, extension in enumerate(extensionTypes):
            if file_extension == extension:
                destination_folder = foldersToMake[i]
                destination_path = os.path.join(directory, destination_folder, file)
                
                
                shutil.move(file_path, destination_path)
                print(f"Moved: {file_path} to {destination_path}")
                break  
