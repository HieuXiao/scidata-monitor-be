from fastapi import APIRouter

router = APIRouter()

@router.post("/token")
async def login():
    return {"access_token": "stub", "token_type": "bearer"}
