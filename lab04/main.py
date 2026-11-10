import sys
from stats import average_by_city, parse_record, read_valid

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

averages = average_by_city(records)
print(len(records))
print(skipped)
print(f"{max(averages.values()):.1f}" if averages else "0.0")
