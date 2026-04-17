import sys, os
import json

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir))

if project_root not in sys.path:
    sys.path.insert(0, project_root)

from utils import Cryptography

class JSONStorage:
    def __init__(self, file):
        super().__init__()
        self.file = file
        self.cryptographer = Cryptography()
        
    def load_data(self):
        try: 
            with open(self.file, 'r') as f:
                return json.load(f)
        except:
            return {}
        
    def save_data(self, data):
        with open(self.file, 'w') as f:
            json.dump(data, f, indent=4)
        
    def add_entry(self, site, key, value):
        
        data = self.load_data()

        encryped_key = self.cryptographer.perform_encrypt(key)
        encryped_value = self.cryptographer.perform_encrypt(value)
        data[site] = {'username': encryped_key, 'password': encryped_value}

        self.save_data(data)
        
    def get_entry(self, title):
        
        data = self.load_data()

        if title not in data:
            raise ValueError("given title not found!")
        
        token = data.get(title)
        decrypted_key = self.cryptographer.perform_decrypt(token=token['username'])
        decrypted_value = self.cryptographer.perform_decrypt(token=token['password'])
        
        return decrypted_key, decrypted_value
        
    def delete_key(self, title):
        
        data = self.load_data()
        
        if title not in data:
            raise ValueError("title not found!")
        
        deleted_title = data[title]
        del deleted_title
        
        self.save_data(data)
        
        return deleted_title