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
