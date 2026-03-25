from neo4j import AsyncGraphDatabase

from app.core.config import get_settings

settings = get_settings()

class Neo4jDriver:
    _driver = None

    @classmethod
    async def get_driver(cls):
        if cls._driver is None:
            cls._driver = AsyncGraphDatabase.driver(
                settings.NEO4J_URI,
                auth=(settings.NEO4J_USERNAME, settings.NEO4J_PASSWORD)
            )
        return cls._driver

    @classmethod
    async def close(cls):
        if cls._driver:
            await cls._driver.close()
            cls._driver = None
