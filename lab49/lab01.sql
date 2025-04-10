CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    full_name TEXT NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    age INTEGER,
    is_active BOOLEAN DEFAULT TRUE
);

INSERT INTO users (full_name, email, age, is_active) VALUES
('Alice Johnson', 'alice@example.com', 29, TRUE),
('Bob Smith', 'bob@example.com', 35, TRUE),
('Carol White', 'carol@example.com', 42, FALSE);