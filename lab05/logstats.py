LEVELS = {"DEBUG", "INFO", "WARNING", "ERROR"}


def parse_event(line: str) -> dict:
    parts = line.strip().split(None, 2)
    if len(parts) != 3:
        raise ValueError(f"expected 3 parts, got {len(parts)}")
    time, level, message = parts
    if level not in LEVELS:
        raise ValueError(f"unknown level: {level}")
    return {"time": time, "level": level, "message": message}


def count_levels(lines) -> dict:
    counts = {}
    for line in lines:
        if not line.strip():
            continue
        try:
            level = parse_event(line)["level"]
        except ValueError:
            level = "BROKEN"
        counts[level] = counts.get(level, 0) + 1
    return counts
