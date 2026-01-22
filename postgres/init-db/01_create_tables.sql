CREATE TABLE IF NOT EXISTS currency_types (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS player_platforms (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS players_currency_log (
    id SERIAL PRIMARY KEY,
    player_uid VARCHAR(100) NOT NULL,
    currency_type_id INTEGER NOT NULL,
    amount_delta INTEGER NOT NULL,
    player_platform_id INTEGER NOT NULL,
    created_at TIMESTAMP DEFAULT NOW()
);

ALTER TABLE players_currency_log ADD CONSTRAINT fk_currency_type 
FOREIGN KEY (currency_type_id) REFERENCES currency_types(id);

ALTER TABLE players_currency_log ADD CONSTRAINT fk_player_platform 
FOREIGN KEY (player_platform_id) REFERENCES player_platforms(id);

CREATE INDEX IF NOT EXISTS idx_player_uid ON players_currency_log(player_uid);
CREATE INDEX IF NOT EXISTS idx_created_at ON players_currency_log(created_at);
CREATE INDEX IF NOT EXISTS idx_currency_type ON players_currency_log(currency_type_id);
CREATE INDEX IF NOT EXISTS idx_platform ON players_currency_log(player_platform_id);