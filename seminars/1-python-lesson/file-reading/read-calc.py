import sys

count = {}
text = sys.stdin.read()

parts = []

for word in text.split(' '):
    parts.append(word.decode('utf-8'))

for word in parts:
    if word not in count.keys():
        count[word] = 0
    count[word] = count[word] + 1


print (count)
