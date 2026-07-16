from collections.abc import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession
from source.config.settings.database import AsyncSessionLocal

async def get_database() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionLocal as session:
        yield session