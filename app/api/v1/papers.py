from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def list_papers():
    return []

@router.get("/{paper_id}")
async def get_paper(paper_id: int):
    return {"id": paper_id, "title": "Placeholder"}
