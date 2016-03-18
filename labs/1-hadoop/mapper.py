#!/usr/bin/python

import sys

#f = open('myfile','w')

for line in sys.stdin:
    fields = line.split(",")
    print fields[2].strip() + ',' + fields[4].strip()
#    f.write('request with line: ' + line)

#f.close()