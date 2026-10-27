SELECT id,visit_date,people
FROM (
    SELECT *,
           LEAD(id, 1) OVER (ORDER BY id) AS next_id,
           LEAD(id, 2) OVER (ORDER BY id) AS next_id2,
           LAG(id, 1) OVER (ORDER BY id) AS prev_id,
           LAG(id, 2) OVER (ORDER BY id) AS prev_id2
    FROM stadium
    WHERE people >= 100
) AS t
WHERE (next_id = id + 1 AND next_id2 = id + 2)
   OR (prev_id = id - 1 AND next_id = id + 1)
   OR (prev_id = id - 1 AND prev_id2 = id - 2)
ORDER BY visit_date;