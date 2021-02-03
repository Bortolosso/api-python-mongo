from fastapi import FastAPI, Body
from src.routes.notice import router as NoticeRouter

app = FastAPI()

app.include_router(NoticeRouter, tags=["Notice"], prefix="/notice")

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}

