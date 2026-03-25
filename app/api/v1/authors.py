from fastapi import APIRouter

router = APIRouter()

@router.get("/{author_id}/graph")
async def get_author_graph(author_id: int):
    return {"nodes": [], "edges": []}
