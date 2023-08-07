# Write your MySQL query statement below
select p.firstName,p.lastName,A.city, A.state
from Person P left JOIN Address A USING(personId)