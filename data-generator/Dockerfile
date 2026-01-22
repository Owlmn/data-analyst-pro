# Этап 1: Сборка зависимостей
FROM python:3.11.2-slim AS builder

WORKDIR /app

# Установка переменных окружения для оптимизации работы Python
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Установка системных зависимостей
RUN apt-get update && apt-get install --no-install-recommends -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Копирование зависимостей и установка
COPY requirements.txt ./
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

# Этап 2: Финальный образ
FROM python:3.11-slim

WORKDIR /app

# Установка переменных окружения для оптимизации работы Python
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Копирование установленных зависимостей из builder
COPY --from=builder /install /usr/local

# Копирование исходного кода
COPY generator.py ./
COPY config.py ./

# Запуск генератора
CMD ["python", "generator.py"]