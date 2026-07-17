from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from source.api.dependencies.database import get_database
from source.repository.user_repository import UserRepository
from source.services.user_service import UserService

def get_user_service(db : AsyncSession = Depends(get_database)) -> UserService :
    respository = UserRepository(db)
    return UserService(respository)