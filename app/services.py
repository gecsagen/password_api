"""Модуль с функциями сервиса."""

from asyncpg import Pool
from .schemas import PasswordCreate
from .utils import encrypt_password, decrypt_password


async def create_password(pool: Pool, service_name: str, password: PasswordCreate):
    """Создание пароля."""
    encrypted_password = encrypt_password(password.password)
    async with pool.acquire() as connection:
        await connection.execute(
            "INSERT INTO passwords (service_name, encrypted_password) VALUES ($1, $2) "
            "ON CONFLICT (service_name) DO UPDATE SET encrypted_password = EXCLUDED.encrypted_password",
            service_name,
            encrypted_password,
        )
    return {"service_name": service_name, "password": password.password}


async def get_password(pool: Pool, service_name: str):
    """Получение пароля."""
    async with pool.acquire() as connection:
        row = await connection.fetchrow(
            "SELECT service_name, encrypted_password FROM passwords WHERE service_name = $1",
            service_name,
        )
    if row:
        return {
            "service_name": row["service_name"],
            "password": decrypt_password(row["encrypted_password"]),
        }
    return None


async def search_passwords(pool: Pool, part_of_service_name: str):
    """Поиск паролей."""
    async with pool.acquire() as connection:
        rows = await connection.fetch(
            "SELECT service_name, encrypted_password FROM passwords WHERE service_name LIKE $1",
            f"%{part_of_service_name}%",
        )
    return [
        {
            "service_name": row["service_name"],
            "password": decrypt_password(row["encrypted_password"]),
        }
        for row in rows
    ]
