from fastapi import APIRouter

from app.api.v1 import (
    auth,
    authors,
    health,
    institutions,
    papers,
    search,
    topics,
    trends,
)

api_router = APIRouter()
api_router.include_router(health.router, prefix="/health", tags=["health"])
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(papers.router, prefix="/papers", tags=["papers"])
api_router.include_router(authors.router, prefix="/authors", tags=["authors"])
api_router.include_router(topics.router, prefix="/topics", tags=["topics"])
api_router.include_router(trends.router, prefix="/trends", tags=["trends"])
api_router.include_router(search.router, prefix="/search", tags=["search"])
api_router.include_router(institutions.router, prefix="/institutions", tags=["institutions"])
