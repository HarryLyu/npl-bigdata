create database movies_igorlyubimov;

use movies_igorlyubimov;

create external table movies (
movie_id int,
movie_title string,
release_date string,
video_release_date string,
IMDbURL string,
unknown int,
Action int,
Adventure int,
Animation int,
Childrens int,
Comedy int,
Crime int,
Documentary int,
Drama int,
Fantasy int,
FilmNoir int,
Horror int,
Musical int,
Mystery int,
Romance int,
SciFi int,
Thriller int,
War int,
Western int
)
row format delimited
fields terminated by '\|'
location '/user/igor.lyubimov/movies';




CREATE  TABLE users
(
user_id int,
age int,
gender string,
occupation string,
zip string
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY '|';

CREATE  TABLE rating(
user_id int,
item_id int,
rating int)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY '\t';

load data inpath '/user/igor.lyubimov/hive-data/users.txt' into table users;
load data inpath '/user/igor.lyubimov/hive-data/rating.txt' into table rating;


create external table movies_short
(
movie_id int,
movie_title string,
release_date string
)
row format delimited
fields terminated by '\|'
location '/user/igor.lyubimov/movies';
