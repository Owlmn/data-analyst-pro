CREATE TABLE players_currency_log (
    id SERIAL PRIMARY KEY,
    player_uid VARCHAR(10) NOT NULL,
    currency_type_id INT REFERENCES currency_types(id),
    amount_delta INTEGER NOT NULL,
    player_platform_id INT REFERENCES player_platforms(id),
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE currency_types (
    id SERIAL PRIMARY KEY,
    currency_name VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE player_platforms (
    id SERIAL PRIMARY KEY,
    platform_name VARCHAR(50) NOT NULL UNIQUE
);