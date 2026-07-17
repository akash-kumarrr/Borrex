from datetime import datetime, timezone, timedelta
import jwt
from source.config.settings.config import get_settings

settings= get_settings()

def create_access_token(data : dict) :
    payload = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=settings.token_expire_minutes)
    payload.update(
        {
            "exp" : expire
        }
    )

    return jwt.encode(payload, settings.secret_key, algorithm=settings.token_algorithm)

def verify_token(token : str) :
    try:
        payload = jwt.encode(
            token, settings.jwt_secret_key, algorithms=[settings.token_algorithm]
        )
        return payload
    except jwt.PyJWTError:
        return None
    
def create_refresh_token(data : dict):
    payload = dict.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=settings.token_expire_minutes)
    payload.update(
        {
            "exp" : expire
        }
    )
    return jwt.encode(payload, settings.jwt_secret_key, algorithm=settings.token_expire_minutes)