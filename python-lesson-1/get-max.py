s = {'vk': 10.5, 'fb': 12, 'google': 7}

max_key = 0

for key in s.keys():
    if s[key] > max_key:
        max_key = key

print 'Max key: ' + max_key