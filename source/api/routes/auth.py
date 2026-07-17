from fastapi import APIRouter, Depends

from source.api.dependencies.auth import get_user_service
from source.models.schemas.user import UserCreate, UserResponse
from source.services.user_service import UserService

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/register", response_model=UserResponse)
async def register(
    data: UserCreate,
    service: UserService = Depends(get_user_service),
):
    user = await service.register(data)
    return user