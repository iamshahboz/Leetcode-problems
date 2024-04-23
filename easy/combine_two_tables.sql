/*

You have Person table with

personId int 
lastName varchar
firstName varchar 

and Address table with 

addressId int 
personId int 
city varchar 
state varchar 

You have to get this result 

firstName lastName city             state
Allen     Wang     Null             Null
Bob       Alice    New York City    New York

*/

SELECT p.firstName, p.lastName, a.city, a.state
FROM Person p
LEFT JOIN Address a ON p.PersonId = a.personId;
