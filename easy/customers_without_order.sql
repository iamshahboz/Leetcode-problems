/*
Imagine you have Customers table with
id (primary_key)
name

and Orders table with
id
customerId(foreign key)

Write a Solution to find all Customers who never ordered anything



*/

SELECT c.name as Customers
FROM Customers c 
LEFT JOIN Orders o on c.id = o.customerId
WHERE o.id IS NULL;

/* this is another solution */


SELECT id, name
FROM Customers c
WHERE NOT EXISTS (
    SELECT 1
    FROM Orders o
    WHERE o.customerId = c.id
);
