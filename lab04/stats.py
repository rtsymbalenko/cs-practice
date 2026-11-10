def parse_record(line: str) -> dict:
    parts = line.split(";")
    if len(parts) != 3:
        raise ValueError(f"expected 3 fields, got {len(parts)}")
    city, temp, date = (p.strip() for p in parts)
    if not city or not date:
        raise ValueError("empty city or date")
    try:
        temperature = float(temp.replace(",", "."))
    except ValueError:
        raise ValueError(f"invalid temperature: {temp!r}") from None
    return {"city": city, "temperature": temperature, "date": date}
