import hashlib

class Auth:
    def __init__(self, file):
        super().__init__()
        self.file = file
        
    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()
        
    def save_file(self, hashed_pass):
            with open('master.key', 'w') as f:
                f.write(hashed_pass)
    
    def set_master_passowrd(self):
        password = str(input("Set master password: "))
        hashed = self.hash_password(password)
        
        self.save_file(hashed_pass=hashed)
        
    def autheticate(self):
        password = str(input("Enter master password: "))
        hashed = self.hash_password(password)
        
        try: 
            with open('master.key', 'r') as f:
                stored_master_pass = f.read()
                
            if stored_master_pass == hashed:
                return True
            
            else:
                print("Wrong password")
                return False
            
        except FileNotFoundError:
            print("No master password is set yet. \n GENERATING...")
            self.set_master_passowrd()
            print("MASTER PASSWORD GENERATED SUCCESSFULLY!")
            return True
        