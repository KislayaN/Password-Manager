# Loads data from file
# Save data to file
# Add / get / delete entries 

import sys, os
import json

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir))

if project_root not in sys.path:
    sys.path.insert(0, project_root)

from utils import Cryptography

class Store:
    def __init__(self):
        super().__init__()
        self.key = None
        self.value = None
        self.title = None
        self.cryptographer = Cryptography()
        
    def add(self, key, value, title):
        self.key = key
        self.value = value
        self.title = title
        
        with open("data.json", "r") as f:
            data = json.load(f)

        encryped_key = self.cryptographer.perform_encrypt(key)
        encryped_value = self.cryptographer.perform_encrypt(value)
        data[title] = {'username': encryped_key, 'password': encryped_value}

        with open("data.json", "w") as f:
            json.dump(data, f, indent=4)
        
    def get(self, title, key):
        self.key = key
        self.title = title
        
        with open("data.json", "r") as f:
            data = json.load(f)

        token = data.get(title, {}).get(key)
        decrypted_key = self.cryptographer.perform_decrypt(token=token)
        
        return decrypted_key
        
    def delt(self, title):
        self.title = title
        
        with open("data.json", "r") as f:
            data = json.load(f)
            
            if title not in data:
                raise ValueError("given title not found!")
            
            else: 
                del data[title]
            
            with open("data.json", 'w') as f:
                json.dump(data, f, indent=4)
            
method = Store()

title = str(input("Enter the title: "))
key = str(input("Enter the username: "))
value = str(input("Enter the password: "))

method.add(title=title,
                 key=key,
                 value=value)

method.delt(title='Twitter')