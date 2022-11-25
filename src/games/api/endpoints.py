from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def get_games():
    return {"message": "games index"}

@router.get("/{game_id}")
async def get_game_by_id(game_id: str):
    return {"message": "specific game"}