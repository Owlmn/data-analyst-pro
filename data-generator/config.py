import os
from dotenv import load_dotenv

load_dotenv()

# Конфигурация подключения к БД
DB_CONFIG = {
    'host': os.getenv('POSTGRES_HOST', 'postgres'),
    'port': os.getenv('POSTGRES_PORT', '5432'),
    'database': os.getenv('POSTGRES_DB', 'game_currency'),
    'user': os.getenv('POSTGRES_USER', 'admin'),
    'password': os.getenv('POSTGRES_PASSWORD', '12345')
}

# Конфигурация генератора данных
GENERATOR_CONFIG = {
    'sleep_interval': 1,
    'servers_count': 4,
    'players_per_server': 3000,
}