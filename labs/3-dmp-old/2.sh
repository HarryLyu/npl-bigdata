#!/usr/bin/env bash
hadoop fs -rm -r -f /user/igor.lyubimov/lab-3-final/
hadoop jar hadoop-streaming.jar \
        -input s3n://datalabs2.npl/lab03data/ \
        -output /user/igor.lyubimov/lab-3-final \
        -mapper 'python mapper-2.py' \
        -reducer 'cat' \
        -file scripts/labs/3-dmp/mapper-2.py \
        -file data/lab-3/user-categories.txt