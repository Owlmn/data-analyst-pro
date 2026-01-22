# Мини-система сбора и анализа данных по внутриигровой статистике
___

## Описание проекта
Проект включает PostgreSQL базу данных, сервер Redis, дашборд Redash для визуализации данных и кастомный генератор данных.

## Установка
Для установки проекта выполните следующие шаги:

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/Y-uri-K/Data-analysis.git
   ```


2. Создайте файл `.env` в корневой директории на основе примера и заполните необходимые переменные окружения:
   ```env
   POSTGRES_DB=your_database_name
   POSTGRES_USER=your_username
   POSTGRES_PASSWORD=your_password
   POSTGRES_HOST=postgres
   POSTGRES_PORT=5432

   REDASH_SECRET_KEY=your_redash_secret_key
   REDASH_COOKIE_SECRET=your_redash_cookie_secret
   REDASH_DATABASE_URL=postgresql://your_username:your_password@postgres:5432/your_database_name
   REDASH_REDIS_URL=redis://redis:6379/0
   ```

   Для генерации `REDASH_SECRET_KEY` и `REDASH_COOKIE_SECRET` используйте следующую команду:
   ```bash
   python -c "import secrets; print(secrets.token_hex(32))"
   ```

## Запуск проекта

1. Для первого запуска инициализируйте базу данных Redash:
   ```bash
   docker compose run --rm redash-server create_db
   ```

2. Запуск:
   ```bash
   docker compose up -d
   ```

3. Доступ к сервисам:
   - **Дашборд Redash**: [http://localhost:5000](http://localhost:5000)

