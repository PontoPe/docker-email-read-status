from fastapi import FastAPI, Response
import redis
import psycopg2
import os

app = FastAPI()
cache = redis.Redis(host='redis', port=6379)

# A transparent 1x1 pixel in base64
PIXEL_DATA = (
    b"\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01\x00\x00\x00\x01"
    b"\x08\x06\x00\x00\x00\x1f\x15\xc4\x89\x00\x00\x00\nIDATx\x9cc\x00\x01"
    b"\x00\x00\x02\x00\x01\xe6\xaf\xc4\xb1\x00\x00\x00\x00IEND\xaeB`\x82"
)

@app.get("/track/{email_id}")
def track_email(email_id: str):
    # 1. Log the 'open' in Redis (Fast/Real-time)
    cache.incr(f"opens:{email_id}")
    
    # 2. Return the invisible pixel
    return Response(content=PIXEL_DATA, media_type="image/png")

@app.get("/stats/{email_id}")
def get_stats(email_id: str):
    count = cache.get(f"opens:{email_id}")
    return {
        "email_id": email_id,
        "total_opens": int(count) if count else 0
    }
