from cryptography.fernet import Fernet

# Генерация ключа шифрования
key = Fernet.generate_key()
cipher_suite = Fernet(key)


def encrypt_password(password: str) -> str:
    """Шифрование пароля."""
    return cipher_suite.encrypt(password.encode()).decode()


def decrypt_password(encrypted_password: str) -> str:
    """Дешифрование пароля."""
    return cipher_suite.decrypt(encrypted_password.encode()).decode()
