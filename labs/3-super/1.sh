#!/usr/bin/env bash
hadoop fs -rm -r -f /user/igor.lyubimov/3s/
hadoop jar hadoop-streaming.jar -Dmapred.reduce.tasks=0  \
        -input s3n://datalabs2.npl/lab03data/ \
        -output /user/igor.lyubimov/3s \
        -mapper 'python mapper-1.py' \
        -file scripts/labs/3-super/mapper-1.py \
        -file data/auto-users.txt