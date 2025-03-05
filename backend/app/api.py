from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
    return {"message": "Connection Established to FastAPI !"}


@app.get("/users")
async def get_users():
    return {"users": ["user1"]}
