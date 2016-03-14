import sys

for line in sys.stdin:
    name, score = line.split("\t")
    print("{0:.1f}".format(round(float(score),1))) + "\t1"