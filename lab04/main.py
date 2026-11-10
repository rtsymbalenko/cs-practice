import sys
from stats import average_by_city, parse_record, read_valid, warmest_city

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

if records:
    averages = average_by_city(records)
    print(f"{averages[warmest_city(records)]:.1f}")
else:
    print("0.0")
