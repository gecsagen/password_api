from . import settings
import asyncpg


async def get_pool():
    """Пул для подключений к БД."""
    pool = await asyncpg.create_pool(settings.REAL_DATABASE_URL)
    yield pool
    await pool.close()
