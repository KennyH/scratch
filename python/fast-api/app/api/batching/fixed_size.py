# app/api/batching/fixed_size.py
from fastapi import APIRouter
import asyncio

router = APIRouter()

batch = []
lock = asyncio.Lock() # protect the batch from race conditions.

@router.post("/batch/fixed-size")
async def add_item(item: str, batch_size: int = 5) -> dict:
    async with lock:
        batch.append(item)
        if len(batch) >= batch_size:
            flushed = batch.copy()
            batch.clear()
            return {"flushed_batch": flushed}
    return {"message": "Item added to batch", "current_size": len(batch)}
