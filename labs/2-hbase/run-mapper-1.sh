#!/usr/bin/env bash
hadoop fs -rm /user/igor.lyubimov/lab-2/*
hadoop fs -rmdir /user/igor.lyubimov/lab-2
hadoop jar hadoop-streaming.jar  -Dmapred.reduce.tasks=1 -input s3n://datalabs2.npl/facetz_2015_02_11 -output /user/igor.lyubimov/lab-2 -mapper 'python mapper-1.py' -file ~/scripts/labs/2-hbase/mapper-1.py
hadoop fs -cat /user/igor.lyubimov/lab-2/* > mapper_result.txt