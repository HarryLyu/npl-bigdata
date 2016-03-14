#!/usr/bin/env bash
cat /Users/igor/work/igor.lyubimov/npl/student_scores.txt | python mapper.py | sort -k1,1 | python reducer.py > result.txt
cat result.txt | python mapper-1.py | sort -k1,1 | python reducer-1.py