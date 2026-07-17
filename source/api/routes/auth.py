from fastapi import APIRouter, status, HTTPException

from sqlalchemy.ext.asyncio import AsyncSession

from source.models.schemas.user import UserCreate, TokenResponse, UserLoginViaEmail, UserCreateResponse

router = APIRouter(
    prefix="/user-auth",
    tags=["User Authentification"]
)

@router.post("/register", response_model=UserCreateResponse, status_code=status.HTTP_201_CREATED)
async def register(user : UserCreate):
    try :
        return user
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    except HTTPException:
        raise

@router.post("/user-login", response_model=TokenResponse, status_code=status.HTTP_200_OK)
async def login(credentials : UserLoginViaEmail):
    try:
        print("under-development")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    except HTTPException:
        raise
