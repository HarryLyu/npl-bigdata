#!/usr/bin/python
#import happybase
import sys

table_name = 'igor.lyubimov'

#connection = happybase.Connection('localhost')
#table = connection.table(table_name)

def is_valid_data (data):
    return data != '' and data != '-'

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) == 3:
        uid, date, url = data
        if is_valid_data(uid) and is_valid_data(date) and is_valid_data(url):
            uid = int(uid)
            date = float(date)
            if uid % 256 == 50:
                print str(uid) + '\t' + str(date) + '\t' + url

#table.put('r12', {'column:': 'value'})

#for key, data in table.scan(limit=5):
#    print 'row'
#    print key, data