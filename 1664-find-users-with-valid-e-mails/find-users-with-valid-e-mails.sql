
SELECT *
FROM users
WHERE REGEXP_like(mail, '^[a-zA-Z][a-zA-Z0-9_.-]*@leetcode\\.com$','c')
