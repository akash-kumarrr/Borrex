from typing import Generic, TypeVar
from sqlalchemy.ext.asyncio import AsyncSession
from uuid import UUID
from sqlalchemy import select

ModelType = TypeVar("ModelType")

class BaseRepository(Generic[ModelType]):
    def __init__(self, db : AsyncSession, model:type[ModelType]) :
        self.db = db
        self.model = model 

    async def create(self, obj : ModelType) -> ModelType : 
        try:
            self.db.add(obj)
            await self.db.commit()
            await self.db.refresh(obj)
            return obj
        except : 
            await self.db.rollback()
            raise

    async def get_by_id(self, id : UUID) -> ModelType | None:
        query = select(self.model).where(self.model.id == id)
        result = await self.db.execute(query)
        return result.scalar_one_or_none
    
    async def update(self, obj : ModelType) -> ModelType:
        try:
            await self.db.commit()
            await self.db.refresh(obj)
            return obj
        
        except Exception as e :
            await self.db.rollback()
            raise

    async def delete(self, obj:ModelType) -> None:
        try : 
            await self.db.delete(obj)
            await self.db.commit()
        except Exception as e :
            await self.db.rollback()
            raise