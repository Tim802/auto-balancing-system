import bcrypt

class Encrypt:
    def __init__(self, rawemail, rawpassword):
        self.raw_email = rawemail
        self.raw_password = rawpassword

        self.email_hash = self.encrypt("EMAIL")
        self.password_hash = self.encrypt("PASSWORD")

        self.hashed_data = (self.email_hash, self.password_hash)

    def encrypt(self, id):
        if id == "EMAIL":
            print(f'Raw email: {self.raw_email}')
            self.b_email = self.raw_email.encode('utf-8')
            salt = bcrypt.gensalt()
            self.e_email = bcrypt.hashpw(self.b_email, salt)
            return self.e_email
        
        elif id == "PASSWORD":
            print(f'Raw Password: {self.raw_password}')
            self.b_password = self.raw_password.encode('utf-8')
            salt = bcrypt.gensalt()
            self.e_password = bcrypt.hashpw(self.b_password, salt)
            return self.e_password
        
        else:
            print('Invalid encrypt id: encryption failed')
            return 0
    
    def hash_checker(self, index, stored):
        return bcrypt.checkpw(index, stored.encode())

enc = Encrypt('TestUser', "Password")
print(enc.hashed_data)