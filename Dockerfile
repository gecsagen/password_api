FROM python:3.9

WORKDIR /usr/src/app

# Скопировать requirements.txt из корня проекта
COPY ./requirements.txt /usr/src/app/requirements.txt

RUN pip install --no-cache-dir -r /usr/src/app/requirements.txt

# Скопировать остальную часть приложения
COPY . /usr/src/app

