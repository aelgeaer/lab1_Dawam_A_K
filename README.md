# News API

CRUD API для управления новостями, пользователями и комментариями, построенный на FastAPI.

## Функциональность

- Создание, чтение, обновление и удаление пользователей
- Создание новостей только верифицированными пользователями
- Комментирование новостей
- Полноценное API для всех сущностей

## Технологии

- Python 3.10+
- FastAPI
- SQLAlchemy
- Alembic
- PostgreSQL

## Установка и запуск

1. Клонируйте репозиторий:
```bash
git clone https://github.com/itmo-webdev/lab1_Dawam_A_K.git
cd lab1_Dawam_A_K
```

2. Установите зависимости:
```bash
pip install -r requirements.txt
```

3. Настройте базу данных PostgreSQL и укажите connection string в переменной окружения:
```bash
export DATABASE_URL="postgresql://user:password@localhost/news_db"


4. Примените миграции:
```bash
alembic upgrade head


5. Запустите приложение:
```bash
uvicorn app.main:app --reload


API будет доступно по адресу: http://localhost:8000
Документация API: http://localhost:8000/docs
