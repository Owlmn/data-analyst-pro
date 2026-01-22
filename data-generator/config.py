import os
from dotenv import load_dotenv

load_dotenv()

# Конфигурация подключения к БД
DB_CONFIG = {
    'host': os.getenv('DB_HOST', 'postgres'),
    'port': os.getenv('DB_PORT', '5432'),
    'database': os.getenv('DB_NAME', 'game_currency'),
    'user': os.getenv('DB_USER', 'admin'),
    'password': os.getenv('DB_PASSWORD', '12345')
}

# Конфигурация генератора данных
GENERATOR_CONFIG = {
    'sleep_interval': 1,
    'servers_count': 4,
    'players_per_server': 3000,
}