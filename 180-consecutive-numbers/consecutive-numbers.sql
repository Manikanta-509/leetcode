select distinct num as ConsecutiveNums from
(
    select num,
    lag(num) over(order by id) as prev1,
    lead(num) over(order by id) as next1
    from logs
)as t
where num=prev1
and num=next1