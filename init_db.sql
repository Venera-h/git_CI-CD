-- Создание таблицы
CREATE TABLE IF NOT EXISTS video_cards (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Функция получения всех продуктов
CREATE OR REPLACE FUNCTION get_all_products()
RETURNS TABLE(id INT, name VARCHAR, price DECIMAL, description TEXT, created_at TIMESTAMP)
LANGUAGE SQL
AS $$
    SELECT id, name, price, description, created_at FROM video_cards ORDER BY id;
$$;

-- Функция подсчета продуктов
CREATE OR REPLACE FUNCTION get_products_count()
RETURNS INT
LANGUAGE SQL
AS $$
    SELECT COUNT(*)::INT FROM video_cards;
$$;
