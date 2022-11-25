from fastapi import FastAPI
import games.api.endpoints

app = FastAPI()

app.include_router(games.api.endpoints.router, prefix="/api/v1/games")

@app.get("/")
async def root():
    return {"active": "true"}