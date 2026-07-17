from argon2 import PasswordHasher

hasher = PasswordHasher()

def hash_password(password : str) :
    return hasher.hash(password)

def verify_password(plain_password : str, hashed_password : str) -> bool :
    return hasher.verify(plain_password, hashed_password)