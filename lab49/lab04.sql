
-- Create a products table
CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    price NUMERIC(10, 2),
    stock INTEGER,
    is_discontinued BOOLEAN DEFAULT FALSE
);

-- Insert new product records
INSERT INTO products (name, price, stock, is_discontinued) VALUES
('Laptop', 1200.00, 10, FALSE),
('Mouse', 25.50, 50, FALSE),
('Keyboard', 45.99, 30, TRUE);

-- Update the price of a product
UPDATE products
SET price = 1300.00
WHERE name = 'Laptop';

-- Delete discontinued products
DELETE FROM products
WHERE is_discontinued = TRUE;
