#!/usr/bin/env bash
hadoop fs -rmdir --ignore-fail-on-non-empty /users/adverts/
hadoop jar /opt/cloudera/parcels/CDH/lib/hadoop-mapreduce/hadoop-streaming.jar -D mapred.reduce.tasks=1 -mapper 'python mapper.py' -reducer 'python reducer.py' -file '/home/ubuntu/mapper.py' -file '/home/ubuntu/reducer.py' -input /users/advert/advert.log -output /users/adverts