from fastapi import FastAPI
from app.api.rate_limiters import leaky_bucket
from app.api.websockets import basic

app = FastAPI(
    title="System Design Patterns in FastAPI",
    description="Exploring rate limiters, counter, queues, and other system design patterns.",
    version="0.1.0"
    )


@app.get("/", description="")
async def root() -> dict:
    return {"message": "Testing '/' worked!"}


app.include_router(leaky_bucket.router, prefix="/rate-limiters/leaky-bucket", tags=["Rate Limiter"])

app.include_router(basic.router, prefix="/ws", tages=["WebSockets"])
