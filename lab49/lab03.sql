-- Remove a user by email
DELETE FROM users
WHERE email = 'carol@example.com';

-- Delete all users above a certain age
DELETE FROM users
WHERE age > 40;
