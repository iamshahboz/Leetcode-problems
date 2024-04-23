/*

You have Employee table with 
id 
name 
salary
managerId 

Write a solution to find the employees who earn more than their managers

*/

SELECT name as Employee FROM Employee e1
WHERE salary > (select salary FROM Employee WHERE id = e1.managerId);

/*
There is another faster implementation

*/

SELECT e1.name as Employee
FROM Employee e1
JOIN Employee e2 on e1.managerId = e2.id 
WHERE e1.salary > e2.salary;

