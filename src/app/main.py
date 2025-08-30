from fastapi import FastAPI

app = FastAPI()  # **Must be named `app`**

@app.get("/health")  # Route handler for GET /health
async def health():
    return {"status": "ok"}
