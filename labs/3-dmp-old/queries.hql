create database igorlyubimov_lab3;

use igorlyubimov_lab3;

create external table visits (
uid string,
domain_address string
)
row format delimited
fields terminated by '\|'
location '/user/igor.lyubimov/lab-3';

select uid, domain_address from visits
WHERE domain_address = 'echo.msk.ru'
LIMIT 10;