# Write your MySQL query statement below
select d.name as Department,e.name as Employee,e.salary from 
department d join(
select name,salary,departmentid,
dense_rank() over(partition by departmentid order by salary 
desc) as r from employee ) e
on d.id=e.departmentid
where e.r=1


