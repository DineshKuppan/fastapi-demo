from fastapi import FastAPI, Depends
import redis
import os

# Load environment variables
REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))

# Create Redis connection
redis_client = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)

# Initialize FastAPI app
app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello, FastAPI with Redis!"}

@app.get("/cache/{key}")
async def read_cache(key: str):
    value = redis_client.get(key)
    if value:
        return {"key": key, "value": value}
    return {"error": "Key not found"}

@app.post("/cache/{key}/{value}")
async def write_cache(key: str, value: str):
    redis_client.set(key, value)
    return {"message": f"Key '{key}' set to '{value}'"}
