import sys

from logstats import count_levels

filename = sys.stdin.readline().strip()

with open(filename, encoding="utf-8") as log:
    counts = count_levels(log)

print(sum(counts.values()))
print(counts.get("ERROR", 0))
print(counts.get("BROKEN", 0))
