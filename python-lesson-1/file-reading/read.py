import sys

def magic (line):
    parts = sorted(line.split(' '))
    parts = map(lambda x: x + '    1', parts)
    for word in parts:
        print(word)

for line in sys.stdin:
    magic(line)
