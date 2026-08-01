# Write your MySQL query statement below
select w1.id 
from weather w1
join weather w2
on w1.recordDate = Date_add(w2.recordDate, interval 1 DAY)
where w1.temperature > w2.temperature; 