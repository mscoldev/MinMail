from werkzeug.security import check_password_hash, generate_password_hash

class User():
    
    def __init__(self,  password, email):
        self.password = password
        self.email = email

    @classmethod
    def check_password(self, hashed_password, password):
        return check_password_hash(hashed_password, password)
    
# print(generate_password_hash("password"))