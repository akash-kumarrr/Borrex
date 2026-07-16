from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache

class Settings(BaseSettings):
    app_name : str = "Borrex"
    app_version : str = "1.0.0"
    app_description : str = "Community to borrow things from your neighbours"

    database_url : str
    secret_key : str
    debug : bool = True

    algorithm : str = "HS256"
    model_config = SettingsConfigDict(
        env_file = ".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )

@lru_cache
def get_settings() -> Settings :
    return Settings()