SELECT d.name AS Department,
       e.name AS Employee,
       e.salary AS Salary
FROM Department d
JOIN (
    SELECT name,
           salary,
           departmentId,
           DENSE_RANK() OVER (
               PARTITION BY departmentId
               ORDER BY salary DESC
           ) AS rn
    FROM Employee
) e
ON d.id = e.departmentId
WHERE e.rn <= 3;