import sys
from stats import parse_record, read_valid

lines = sys.stdin.read().splitlines()
records = read_valid(lines)

skipped = 0
for line in lines:
    if not line.strip():
        continue
    try:
        parse_record(line)
    except ValueError:
        skipped += 1

print(len(records))
print(skipped)
print(0.0)
