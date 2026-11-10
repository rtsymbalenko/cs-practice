import sys

from logstats import parse_event

filename = sys.stdin.readline().strip()

total = 0
broken = 0
with open(filename, encoding="utf-8") as log:
    for line in log:
        if not line.strip():
            continue
        total += 1
        try:
            parse_event(line)
        except ValueError:
            broken += 1

print(total)
print(0)
print(broken)
