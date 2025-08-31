from fastapi import FastAPI

app = FastAPI()  # **Must be named `app`**

@app.get("/")  # Route handler for GET /health
async def root():
    return {"status": "ok"}
