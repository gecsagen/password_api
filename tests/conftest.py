import asyncpg
import asyncio
from app import settings
import pytest_asyncio
from app.database import get_pool
from fastapi.testclient import TestClient
from app.main import app
from typing import AsyncGenerator

CLEAN_TABLES = [
    "passwords",
]


@pytest_asyncio.fixture(scope="session")
def event_loop():
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


async def _asyncpg_pool():
    pool = await asyncpg.create_pool(settings.TEST_DATABASE_URL)
    yield pool
    await pool.close()


@pytest_asyncio.fixture(scope="session", autouse=True)
async def clear_database():
    async with asyncpg.create_pool(settings.TEST_DATABASE_URL) as pool:
        async with pool.acquire() as conn:
            for table_for_cleaning in CLEAN_TABLES:
                await conn.execute(f"TRUNCATE TABLE {table_for_cleaning} CASCADE;")


@pytest_asyncio.fixture(scope="function")
async def client() -> AsyncGenerator:
    app.dependency_overrides[get_pool] = _asyncpg_pool
    with TestClient(app) as client:
        yield client