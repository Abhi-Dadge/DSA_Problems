# Write your MySQL query statement below
select user_id,
Concat(UPPER(LEFT(name,1)),
LOWER(SUBSTRING(name,2)))
AS name from Users 
Order by user_id; 
