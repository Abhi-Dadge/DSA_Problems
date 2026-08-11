# Write your MySQL query statement below
SELECT 
    d.name As Department,
    e.name As Employee,
    e.salary As Salary
FROM (
    SELECT *, DENSE_RANK() OVER (
        PARTITION BY departmentId
        ORDER BY salary DESC
    ) AS rnk
FROM Employee
) e 
JOIN Department d
    ON e.departmentId = d.id
WHERE e.rnk <= 3;