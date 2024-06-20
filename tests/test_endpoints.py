"""Тесты для api."""

import pytest
from fastapi.testclient import TestClient


@pytest.mark.asyncio
async def test_create_password(client: TestClient):
    response = client.post(
        "/password/test_service",
        json={"password": "test_password"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["service_name"] == "test_service"
    assert data["password"] == "test_password"


@pytest.mark.asyncio
async def test_read_password(client: TestClient):
    # Создаем пароль сначала
    client.post(
        "/password/test_service",
        json={"password": "test_password"}
    )
    
    # Теперь читаем его
    response = client.get("/password/test_service")
    assert response.status_code == 200
    data = response.json()
    assert data["service_name"] == "test_service"
    assert data["password"] == "test_password"


@pytest.mark.asyncio
async def test_search_passwords(client: TestClient):
    # Создаем несколько паролей сначала
    client.post(
        "/password/service1",
        json={"password": "password1"}
    )
    client.post(
        "/password/service2",
        json={"password": "password2"}
    )
    
    # Теперь ищем пароли по части имени сервиса
    response = client.get("/password/?service_name=service")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 3
    assert data[0]["service_name"] == "test_service"
    assert data[1]["service_name"] == "service1"
    assert data[2]["service_name"] == "service2"