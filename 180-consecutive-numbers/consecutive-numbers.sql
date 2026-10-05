SELECT DISTINCT num AS ConsecutiveNums
FROM (
    SELECT 
        num,
        LAG(num) OVER(ORDER BY id) AS prev1,
        LEAD(num) OVER(ORDER BY id) AS next1
    FROM Logs
) t
WHERE num = prev1
  AND num = next1;