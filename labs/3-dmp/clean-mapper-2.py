import sys

prev_key = None
data = []
for line in sys.stdin:
    data = line.strip().split("\t")
    uid = data[0]
    if uid != prev_key and prev_key is not None:
        print "\t".join(data)
    prev_key = uid