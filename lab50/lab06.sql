-- Retrieve all employees sorted by first name (A-Z)
SELECT * FROM employees ORDER BY first_name ASC;

-- Retrieve all employees sorted by salary (highest to lowest)
SELECT * FROM employees ORDER BY salary DESC;

-- Retrieve employees sorted by department (A-Z), then by salary (highest first)
SELECT * FROM employees ORDER BY department ASC, salary DESC;