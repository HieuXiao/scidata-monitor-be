from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def list_topics():
    return []

@router.get("/scatter")
async def get_topic_scatter():
    return []
