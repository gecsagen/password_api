# Менеджер Паролей

## Описание

Это простой API для менеджера паролей, который хранит зашифрованные пароли в базе данных PostgreSQL. API позволяет создавать, получать и искать пароли, привязанные к имени сервиса.

## Требования

- Docker
- Docker Compose

## Как запустить проект

1. Клонируйте репозиторий:
   ```sh
   git clone https://github.com/gecsagen/password_api.git  
   cd password_api  
   ```

2. Запустите контейнеры Docker:
   ```sh
   docker-compose up --build
   ```

3. API будет доступно по адресу: [http://localhost:8004](http://localhost:8004)


## Использование API

### Создание пароля для сервиса

**Запрос:**

```http
POST /password/{service_name}
Content-Type: application/json

{
  "password": "your_password"
}
```

**Ответ:**

```http
HTTP/1.1 200 OK
Content-Type: application/json

{
  "service_name": "{service_name}",
  "password": "your_password"
}
```

### Получение пароля для сервиса

**Запрос:**

```http
GET /password/{service_name}
Accept: application/json
```

**Ответ:**

```http
HTTP/1.1 200 OK
Content-Type: application/json

{
  "service_name": "{service_name}",
  "password": "your_password"
}
```

### Поиск паролей по части имени сервиса

**Запрос:**

```http
GET /password/?service_name={part_of_service_name}
Accept: application/json
```

**Ответ:**

```http
HTTP/1.1 200 OK
Content-Type: application/json

[
  {
    "service_name": "{service_name}",
    "password": "your_password"
  }
]
```
