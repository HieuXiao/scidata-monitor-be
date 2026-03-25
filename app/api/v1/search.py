from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def search_papers(q: str):
    return []
