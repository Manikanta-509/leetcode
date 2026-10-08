SELECT s.student_id,
       s.student_name,
       st.subject_name,
       COUNT(e.student_id) AS attended_exams
FROM students s
CROSS JOIN subjects st
LEFT JOIN examinations e
ON s.student_id = e.student_id
AND st.subject_name = e.subject_name
GROUP BY s.student_id,
         s.student_name,
         st.subject_name
ORDER BY s.student_id,
         st.subject_name;