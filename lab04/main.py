import sys
from stats import parse_record

lines = sys.stdin.read().splitlines()

valid = 0
skipped = 0
for line in lines:
    if not line.strip():
        continue
    try:
        parse_record(line)
        valid += 1
    except ValueError:
        skipped += 1

print(valid)
print(skipped)
print(0.0)
