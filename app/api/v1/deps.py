from app.db.neo4j.driver import Neo4jDriver
from app.db.postgres.session import get_async_session


async def get_db():
    async for session in get_async_session():
        yield session

async def get_neo4j():
    return await Neo4jDriver.get_driver()
