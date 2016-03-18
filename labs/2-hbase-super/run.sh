#!/usr/bin/env bash
hadoop fs -cat /user/igor.lyubimov/lab-2-super/* > lab-2-super-res.txt
cat lab-2-super-res.txt | sort -nrk2,2 > lab-2super.txt
head -n 350 lab-2super.txt > top350.txt