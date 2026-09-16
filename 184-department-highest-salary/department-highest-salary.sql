select d.name as 'Department',
e.name as 'Employee',
e.salary as 'Salary'
from department d
join(
    select name,salary,departmentid,
    dense_rank() over(partition by departmentid order by salary desc) as rn from employee 
)e
on d.id=e.departmentid
where e.rn=1