import sys
import math

for line in sys.stdin:
    data = line.strip().split(",")
    print data[0] + "\t" + data[3]
