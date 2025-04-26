from fastapi import APIRouter

router = APIRouter()

@router.get("/", description="Leaky Bucket rate limiter.")
async def leaky_bucket():
    return {"message": "TODO"}
