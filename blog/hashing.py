from passlib.context import CryptContext

pwd_context  = CryptContext(schemes=["bcrypt"], deprecated="auto")
class Hashing:
    # def __init__(self):
    #     self.context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def encrypt_password(password):
        return pwd_context.hash(password)
    
    def verify_password(password, hashed_password):
        return pwd_context.verify(password, hashed_password)
    
    def decrypt_password(password):
        return pwd_context.unhash(password)