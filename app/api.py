from fastapi import APIRouter, HTTPException, Depends
from asyncpg import Pool
from . import database, schemas, services


password_router = APIRouter()


@password_router.post(
    "/password/{service_name}", response_model=schemas.PasswordResponse
)
async def create_password(
    service_name: str,
    password: schemas.PasswordCreate,
    pool: Pool = Depends(database.get_pool),
):
    """Создание пароля."""
    new_password = await services.create_password(pool, service_name, password)
    return new_password


@password_router.get(
    "/password/{service_name}", response_model=schemas.PasswordResponse
)
async def read_password(service_name: str, pool: Pool = Depends(database.get_pool)):
    """Получение пароля."""
    db_password = await services.get_password(pool, service_name)
    if db_password is None:
        raise HTTPException(status_code=404, detail="Service not found")
    return db_password


@password_router.get("/password/", response_model=list[schemas.PasswordResponse])
async def search_passwords(service_name: str, pool: Pool = Depends(database.get_pool)):
    """Поиск пароля."""
    passwords = await services.search_passwords(pool, service_name)
    return passwords
