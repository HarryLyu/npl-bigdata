CREATE EXTERNAL TABLE
domain_visits (domain STRING, auto_user INT)
row format delimited fields terminated by '\t' stored as TEXTFILE location '/user/igor.lyubimov/3s';

ALTER_TABLE domain_sums ADD COLUMN (auto_hits INT)

//
CREATE EXTERNAL TABLE domain_sums (domain STRING, c INT);
INSERT OVERWRITE TABLE domain_sums
SELECT domain_visits.domain, count(1) AS count FROM domain_visits GROUP BY domain_visits.domain;
//

//
DROP TABLE IF EXISTS domain_sums_auto;
CREATE EXTERNAL TABLE domain_sums_auto (domain STRING, c INT);
INSERT OVERWRITE TABLE domain_sums_auto
SELECT domain_visits.domain, count(1) AS count FROM domain_visits WHERE auto_user = 1 GROUP BY domain_visits.domain;
//

SELECT count(*) FROM domain_visits WHERE auto_user = "1";

SELECT count(*) FROM domain_visits WHERE auto_user = "0";
// 313527
// 6257511
// 6571038


DROP TABLE IF EXISTS domain_sums;
CREATE EXTERNAL TABLE domain_sums (domain STRING, hits INT, auto_hits INT);
INSERT OVERWRITE TABLE domain_sums
select domain, count(auto_user) hits, sum(auto_user) auto_hits from domain_visits group by domain order by hits DESC;

SELECT
domain_sums.domain,
domain_sums.hits,
domain_sums.auto_hits,
format_number(pow(domain_sums.auto_hits / 6571038, 2) / ((domain_sums.hits / 6571038) * (313527 / 6571038)), 20) v
FROM domain_sums
ORDER by v DESC
LIMIT 200;