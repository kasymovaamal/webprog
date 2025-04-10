-- Retrieve employees with a salary greater than 60000
SELECT * FROM employees WHERE salary > 60000;

-- Retrieve employees hired after January 1, 2020
SELECT * FROM employees WHERE hire_date > '2020-01-01';

-- Retrieve employees who work in the HR or Finance department
SELECT * FROM employees WHERE department IN ('HR', 'Finance');
