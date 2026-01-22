INSERT INTO currency_types (name) VALUES 
('credits'), ('gems'), ('crystals')
ON CONFLICT (name) DO NOTHING;

INSERT INTO player_platforms (name) VALUES 
('pc'), ('android'), ('ios'), ('playstation'), ('xbox')
ON CONFLICT (name) DO NOTHING;