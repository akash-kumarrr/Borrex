from datetime import datetime, timezone, timedelta
import jwt
from jwt.exceptions import InvalidTokenError
from source.config.settings.config import get_settings

settings= get_settings()

def verify_token(token : str) :
    try:
        payload = jwt.encode(
            token, settings.jwt_secret_key, algorithms=[settings.token_algorithm]
        )
        return payload
    except jwt.PyJWTError:
        return None
    except jwt.InvalidTokenError:
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