import time
import random
import psycopg2
from config import DB_CONFIG, GENERATOR_CONFIG

class CurrencyTransactionGenerator:
    def __init__(self):
        self.conn = None
        self.currencies = []
        self.platforms = []
        
        self.server_count = GENERATOR_CONFIG.get('servers_count', 4)
        self.players_per_server = GENERATOR_CONFIG.get('players_per_server', 250)
        
        self.player_uids = self._generate_player_uids()
        self.current_player_index = 0
        self.transaction_count = 0
    
    # Генерация уникальных player_uid
    def _generate_player_uids(self):
        uids = []
        for server in range(1, self.server_count + 1):
            for player_num in range(1, self.players_per_server + 1):
                uid = f"{server}{player_num:09d}"  # Формат: 4000000567
                uids.append(uid)
        return uids
    
    # Получение следующего player_uid по кругу
    def _get_next_player_uid(self):
        uid = self.player_uids[self.current_player_index]
        self.current_player_index = (self.current_player_index + 1) % len(self.player_uids)
        return uid
    
    # Генерация суммы транзакции с учетом вероятности
    def _generate_transaction_amount(self, currency_name):
        
        base_amounts = {'credits': 1000, 'gems': 50, 'crystals': 100}
        base = base_amounts.get(currency_name)
        
        # 60% пополнений, 40% трат
        if random.random() < 0.6:
            multiplier = random.randint(1, 100)
            return base * multiplier
        else:
            multiplier = random.randint(1, 50)
            return -(base * multiplier)
    
    # Генерация одной транзакции
    def _generate_transaction(self, player_uid):
        
        currency_weights = [0.6, 0.3, 0.1]
        currency = random.choices(self.currencies, weights=currency_weights)[0]
        
        platform = random.choice(self.platforms)
        
        amount = self._generate_transaction_amount(currency[1])
        
        return {
            'player_uid': player_uid,
            'currency_type_id': currency[0],
            'currency_name': currency[1],
            'amount_delta': amount,
            'player_platform_id': platform[0],
            'platform_name': platform[1]
        }
    
    # Подключение к БД
    def connect_to_db(self):
        max_retries = 10
        for i in range(max_retries):
            try:
                self.conn = psycopg2.connect(**DB_CONFIG)
                return True
            except Exception as e:
                time.sleep(2)
        
        return False
    
    # Загрузка вспомогательной инфы из БД
    def load_reference_data(self):
        try:
            with self.conn.cursor() as cur:
                cur.execute("SELECT id, name FROM currency_types ORDER BY id")
                self.currencies = cur.fetchall()
                
                cur.execute("SELECT id, name FROM player_platforms ORDER BY id")
                self.platforms = cur.fetchall()
            return True
        
        except Exception as e:
            return False
    
    # Вставка транзакции в БД
    def insert_transaction(self, transaction):
        try:
            with self.conn.cursor() as cur:
                cur.execute("""
                    INSERT INTO players_currency_log 
                    (player_uid, currency_type_id, amount_delta, player_platform_id)
                    VALUES (%s, %s, %s, %s)
                """, (
                    transaction['player_uid'],
                    transaction['currency_type_id'],
                    transaction['amount_delta'],
                    transaction['player_platform_id']
                ))
                self.conn.commit()
                self.transaction_count += 1
                return True
                
        except Exception as e:
            self.conn.rollback()
            return False
    
    # Генерация и вставка одной транзакции
    def generate_and_insert_transaction(self):
        player_uid = self._get_next_player_uid()
        transaction = self._generate_transaction(player_uid)
        
        self.insert_transaction(transaction)
        
    
    def run(self):
        
        if not self.connect_to_db():
            return
        
        if not self.load_reference_data():
            return
                
        try:
            while True:
                self.generate_and_insert_transaction()
                time.sleep(GENERATOR_CONFIG.get('sleep_interval', 0.5))
                
        except KeyboardInterrupt:
            print("\n Остановка генератора данных...")
        finally:
            if self.conn:
                self.conn.close()
            print(f"Итого: {self.transaction_count} транзакций")

def main():
    generator = CurrencyTransactionGenerator()
    generator.run()

if __name__ == "__main__":
    main()