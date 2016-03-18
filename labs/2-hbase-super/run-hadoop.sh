#!/usr/bin/env bash
#!/usr/bin/env bash
#hadoop fs -rm /user/igor.lyubimov/lab-2-super/*
#hadoop fs -rmdir /user/igor.lyubimov/lab-2-super
hadoop jar hadoop-streaming.jar -input s3n://datalabs2.npl/facetz_2015_02_12 \
        -output /user/igor.lyubimov/lab-2-super \
        -mapper 'python mapper.py' \
        -file ~/scripts/labs/2-hbase-super/mapper.py \
        -reducer 'python reducer.py' \
        -file ~/scripts/labs/2-hbase-super/reducer.py