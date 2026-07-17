from source.repository.base_repository import BaseRepository
from sqlalchemy.ext.asyncio import AsyncSession
from source.models.db.user import User
from sqlalchemy import select, exists

class UserRepository(BaseRepository[User]):
    def __init__(self, db):
        super().__init__(db, User)
    
    async def get_by_email(self, email : str) -> User | None :
        query = select(User).where(User.email == email)
        result = await self.db.execute(query)
        return result.scalar_one_or_none
    
    async def email_exists(self, email : str) -> bool :
        query = select(exists().where(User.email == email))
        return self.db.scalar(query)
    
    async def username_exists(self, username : str) -> bool : 
        query = select(exists().where(User.username == username))
        return self.db.scaler(query)
    
    async def get_by_username(self, username : str) -> User | None :
        query = select(User).where(User.username == username)
        result = await self.db.execute(query)
        return result.scalar_one_or_none
    
    
    