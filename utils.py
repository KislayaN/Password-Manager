# Encryption / Decryption
# input validation
# formatting output

from cryptography.fernet import Fernet
import os

class Cryptography:
    def __init__(self):
        super().__init__()
        self.key = None
        self.fernet = None
    
    def get_key(self):
        if not os.path.exists("key.key"):
            key = Fernet.generate_key()
            self.key = key
        
            with open("key.key", 'wb') as f:
                f.write(self.key)
            
        else:
            with open("key.key", 'rb') as f:
                self.key = f.read()
                
        return self.key
        
    def perform_encrypt(self, text):
        self.key = self.get_key()
        self.fernet = Fernet(self.key)
        return self.fernet.encrypt(text.encode()).decode()
    
    def perform_decrypt(self, token):
        return self.fernet.decrypt(token.encode()).decode()