BEGIN;

-- Insert a new record
INSERT INTO users (full_name, email, age, is_active)
VALUES ('David Brown', 'david@example.com', 28, TRUE);

-- Update an existing record
UPDATE users
SET age = 36
WHERE full_name = 'Bob Smith';

-- Delete a record
DELETE FROM users
WHERE full_name = 'Alice Johnson';

ROLLBACK;