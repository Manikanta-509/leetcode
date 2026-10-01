select user_id,time_stamp as last_stamp from(
    select user_id,time_stamp,dense_rank() over(partition by user_id
    order by time_stamp desc) as r from logins
    where year(time_stamp)=2020
) e
where r=1
