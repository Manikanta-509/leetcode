/*select * from patients where (conditions like 'DIAB1%' or conditions like '% DIAB1%')*/
select * from patients where (conditions like 'diab1%' or conditions like '% diab1%')