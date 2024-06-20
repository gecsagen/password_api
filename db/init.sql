-- Создание таблицы "passwords"
CREATE TABLE IF NOT EXISTS passwords (
    id SERIAL PRIMARY KEY,
    service_name VARCHAR(255) UNIQUE NOT NULL,
    encrypted_password TEXT NOT NULL
);
