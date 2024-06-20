"""Схемы pydantic."""

from pydantic import BaseModel


class PasswordCreate(BaseModel):
    """Схема для создания пароля."""

    password: str


class PasswordResponse(BaseModel):
    """Схема ответа."""

    service_name: str
    password: str

    class Config:
        from_attributes = True
