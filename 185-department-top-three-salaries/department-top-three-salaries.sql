
select d.name as Department,e.name as Employee,e.salary as Salary from department d
join(
    select id,name,salary,departmentid,dense_rank()
    over(partition by departmentid order by salary desc) as r from employee 
)e 
on d.id=e.departmentid
where r<=3