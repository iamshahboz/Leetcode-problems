/* You have Person table, it has id and email fields. Write a solution to get back 
duplicate email. Return it in any order

Input

id     email
1      a@b.com
2      c@b.com
3      a@b.com

Output

email

a@b.com
*/

SELECT email from person GROUP BY email HAVING COUNT(*) > 1;
