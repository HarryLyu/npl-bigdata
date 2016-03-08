#!/usr/bin/env python
from operator import itemgetter
import sys

country_data = {}
country_data_sorted = []

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    country, payout = line.split(',', 1)

    # convert count (currently a string) to int
    try:
        payout = float(payout)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue

    if country not in country_data.keys():
        country_data[country] = 0

    country_data[country] += payout

for key in country_data.keys():
    country_data_sorted.append([key, country_data[key]])

country_data_sorted = sorted(country_data_sorted, key=lambda x: x[1], reverse=True)

for key in country_data_sorted:
    print key[0] + ', ' + str(key[1])