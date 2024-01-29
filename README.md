# Запуск проекта

1. Установить зависимости: `pip install -e .`

2. Применить миграции: `alembic upgrade head`

3. Запустить проект: `uvicorn app.main:app`
