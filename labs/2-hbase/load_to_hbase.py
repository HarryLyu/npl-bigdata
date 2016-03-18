#!/usr/bin/python
#import happybase
#import sys

table_name = 'igor.lyubimov'

lines = open('mapper_result.txt', 'r').read().split("\n")

for line in lines:
    uid, date, url = line.strip().split("\t")
    print "put '" + table_name + "', '" + uid + "', 'data', '" + url + "', " + date

#table.put('r12', {'column:': 'value'})

#for key, data in table.scan(limit=5):
#    print 'row'
#    print key, data