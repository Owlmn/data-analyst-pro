# Мини-система сбора и анализа данных по внутриигровой статистике
___

## Описание проекта
Система описывает внутриигровые логи пользователей связанные с тратой/получением трех типов валюты: credits - стандартная внутригровая валюта, gems - премиальная валюта, crystals - донатная валюта. Также имеются данные о платформе, с которой было совершено действие. Проект включает PostgreSQL базу данных, сервер Redis, дашборд Redash для визуализации данных и кастомный генератор данных.

## Установка
Для установки проекта выполните следующие шаги:

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/Y-uri-K/Data-analysis.git
   ```


2. Создайте файл `.env` в корневой директории на основе примера и заполните необходимые переменные окружения:
   ```
    POSTGRES_DB=
    POSTGRES_USER=
    POSTGRES_PASSWORD=
    POSTGRES_HOST=
    POSTGRES_PORT=

    REDASH_USER=
    REDASH_PASSWORD=
    REDASH_DB_NAME=
   ```


## Запуск проекта

1. Для первого запуска инициализируйте базу данных Redash:
   ```bash
   docker compose run --rm redash-server create_db
   ```

2. Команда запуска:
   ```bash
   docker compose up -d
   ```

3. Доступ к сервисам:
   - **Дашборд Redash**: [http://localhost:5000](http://localhost:5000)

# Проект
## Схема БД 

![Image alt](https://github.com/Owlmn/data-analyst-pro/raw/main/screenshots/db_schema.png)

## Redash Dashboard

![Image alt](https://github.com/Owlmn/data-analyst-pro/raw/main/screenshots/capture_20260122202053779.png)

## Список контейнеров

![Image alt](https://github.com/Owlmn/data-analyst-pro/raw/main/screenshots/containers.png)


