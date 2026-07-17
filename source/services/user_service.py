from fastapi import HTTPException
from source.models.db.user import User
from source.security.hashing.password import hash_password, verify_password
from source.security.authorizations.jwt import create_access_token
from source.models.schemas.user import UserCreate

class AuthService : 
    def __init__(self, user_repository):
        self.user_repository = user_repository
    
    async def register(self, user : UserCreate) :
        email_existing = await self.user_repository.email_exists(user.email)
        if email_existing:
            raise HTTPException(status_code=400, detail="EMail Already exists...")
        
        username_existsing = await self.user_repository.username_exists(user.username)
        if username_existsing:
            raise HTTPException(status_code=400, detail="Username already exists.")
        
        hashed_password = hash_password(user.password)
        
        user = User(
            email=user.email,
            full_name=user.full_name,
            password_hash=hashed_password,
            contact_number=user.contact_number,
            username = user.username
        )