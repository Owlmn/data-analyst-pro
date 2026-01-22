--Средняя сумма покупки/траты валюты среди игроков
SELECT
    ct.name AS currency_name,
    ROUND(AVG(amount_delta), 0) AS avg_per_player
FROM players_currency_log pcl
JOIN currency_types ct ON pcl.currency_type_id = ct.id
GROUP BY ct.name
ORDER BY ct.name DESC;

-- Топ платформ по покупке донат валюты
SELECT
    pp.name AS platform_name,
    SUM(pcl.amount_delta) AS total_crystals
FROM players_currency_log pcl
JOIN player_platforms pp ON pcl.player_platform_id = pp.id
JOIN currency_types ct ON pcl.currency_type_id = ct.id
WHERE ct.name = 'crystals'
  AND pcl.amount_delta > 0
GROUP BY pp.name
ORDER BY total_crystals DESC;

-- График изменения кол-ва валюты у игроков
SELECT
    ct.name AS currency_name,
    DATE_TRUNC('minute', pcl.created_at) AS time,
    SUM(amount_delta) AS net_change
FROM players_currency_log pcl
JOIN currency_types ct ON pcl.currency_type_id = ct.id
GROUP BY ct.name, DATE_TRUNC('minute', pcl.created_at)
ORDER BY ct.name, time;

