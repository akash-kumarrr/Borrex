from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from source.config.settings.config import get_settings

settings = get_settings()

engine = create_async_engine(
    settings.database_url, 
    echo=settings.debug,
    connect_args={
        'ssl' : True
    }
)

AsyncSessionLocal = async_sessionmaker(
    bind = engine,
    class_ = AsyncSession,
    expire_on_commit=False
)