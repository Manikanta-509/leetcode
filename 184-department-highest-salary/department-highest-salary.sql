# Write your MySQL query statement below
select d.name as department,e.name as employee,e.salary from department d join(
    select id,name,salary,departmentid,dense_rank() over(partition by departmentid order by salary desc) as r from employee
)e 
on d.id=e.departmentid
where r=1