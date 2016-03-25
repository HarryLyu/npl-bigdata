#!/usr/bin/env bash
hadoop fs -rm -r -f /user/igor.lyubimov/3/
hadoop jar hadoop-streaming.jar \
        -input s3n://datalabs2.npl/lab03data/ \
        -output /user/igor.lyubimov/3 \
        -mapper 'python mapper-1.py' \
        -file scripts/labs/3-dmp/mapper-1.py \
        -reducer 'python reducer-1.py' \
        -file scripts/labs/3-dmp/reducer-1.py