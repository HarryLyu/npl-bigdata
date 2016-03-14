from __future__ import division
import sys

def do_reduce(word, values):
    average = sum(values) / len(values)
#    print word + " " + str(average)
    return word, average

prev_key = None
values = []

for line in sys.stdin:
    key, value = line.split("\t")
    if key != prev_key and prev_key is not None:
        result_key, result_value = do_reduce(prev_key, values)
        print(result_key + "\t" + str(result_value))
        values = []
    prev_key = key
    values.append(int(value))

if prev_key is not None:
    result_key, result_value = do_reduce(prev_key, values)
    print(result_key + "\t" + str(result_value))