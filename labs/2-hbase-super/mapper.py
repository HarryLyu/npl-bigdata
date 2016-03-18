#!/usr/bin/python
import sys

def is_valid_data (data):
    return data != '' and data != '-'

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) == 3:
        uid, date, url = data
        if is_valid_data(uid) and is_valid_data(url):
            print url + '\t' + '1'