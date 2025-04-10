-- Retrieve employees who work in IT or HR
SELECT * FROM employees WHERE department IN ('IT', 'HR');

-- Retrieve employees whose salary is exactly 48000, 65000, or 72000
SELECT * FROM employees WHERE salary IN (48000, 65000, 72000);

