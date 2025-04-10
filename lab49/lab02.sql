-- Modify a user's age
UPDATE users
SET age = 30
WHERE full_name = 'Alice Johnson';

-- Change an email address
UPDATE users
SET email = 'bobby@example.com'
WHERE full_name = 'Bob Smith';