import sys

from logstats import count_levels, format_report, top_errors

filename = sys.stdin.readline().strip()

with open(filename, encoding="utf-8") as log:
    counts = count_levels(log)

with open(filename, encoding="utf-8") as log:
    errors = top_errors(log, 10)

print(sum(counts.values()))
print(counts.get("ERROR", 0))
print(counts.get("BROKEN", 0))

with open("report.txt", "w", encoding="utf-8") as out:
    out.write(format_report(counts, errors))
