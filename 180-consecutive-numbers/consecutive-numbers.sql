# Write your MySQL query statement below
select distinct num as ConsecutiveNums from(
    select num,
    lead(num) over(order by id) as next,
    lag(num) over(order by id) as prev
    from logs
)as t
where num=next
and num=prev