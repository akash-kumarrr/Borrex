from fastapi import APIRouter, status, HTTPException


router = APIRouter(
    prefix="/health",
    tags=["Backend Health"]
)

@router.get("/", status_code=status.HTTP_200_OK)
async def health():
    try:
        return {
            "message" : "healthy"
        }
    except Exception as e : 
        raise HTTPException(status_code=500, detail=str(e))