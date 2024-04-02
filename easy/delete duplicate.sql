/* Delete duplicate records and leave the min id
the duplicated field is email
*/



delete from Person
where Id not in (select min_id from
(select min(Id) as min_id from Person group by Email) as a)