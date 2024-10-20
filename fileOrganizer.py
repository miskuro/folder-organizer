import os
import shutil
import time
import json
import sys


directory = os.path.dirname(os.path.abspath(__file__))

def type(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.008)


type("INFO : the folders will be created from 'organizers.json' so if you wanna change something, head to the json\n")
type("and change to your preferences \n")

try:
    with open ('organizers.json', 'r') as file:
        automatiqueManagement = json.load(file)
        json_path = os.path.join(directory, "organizers.json")
except FileNotFoundError:
    type("ERROR : the json file is not there, make sure both the script and the json file are in the same directory")
    sys.exit(1)

script_path = os.path.join(directory, "fileOrganizer.py")


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

            
            if file_extension in extensions and file_path != json_path and file_path != script_path:
                destination_folder = os.path.join(folder_path, file)
                shutil.move(file_path, destination_folder)
                print(f"Moved: {file} to {folder_path}")


organize_files()
