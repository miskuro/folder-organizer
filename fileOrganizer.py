import os
import shutil
import time
import json


directory = os.getcwd()

def type(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.008)


type("the folders will be created from 'organizers.json' so if you wanna change something, head to the json\n")
type("and change to your preferences")

with open ('organizers.json', 'r') as file:
    automatiqueManagement = json.load(file)
    json_path = os.path.join(directory, "organizers.json")




def organize_files():
    for category, extensions in automatiqueManagement.items():
        folder_path = os.path.join(directory, category)
        try:
            os.makedirs(folder_path, exist_ok=True)
            print(f"New folder created: {folder_path}")
        except Exception as e:
            print(f"Error creating folder: {e}")

        
        for file in os.listdir(directory):
            _, file_extension = os.path.splitext(file)
            file_path = os.path.join(directory, file)

            
            if file_extension in extensions and file_path != json_path:
                destination_folder = os.path.join(folder_path, file)
                shutil.move(file_path, destination_folder)
                print(f"Moved: {file} to {folder_path}")


organize_files()
