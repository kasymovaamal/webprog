-- Retrieve employees whose first name starts with 'A'
SELECT * FROM employees WHERE first_name LIKE 'A%';

-- Retrieve employees whose last name contains 'son'
SELECT * FROM employees WHERE last_name LIKE '%son%';

-- Retrieve employees whose first name ends with 'e'
SELECT * FROM employees WHERE first_name LIKE '%e';