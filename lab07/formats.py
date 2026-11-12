import json


def csv_to_records(text: str) -> list[dict]:
    lines = [line for line in text.strip().splitlines() if line.strip()]
    if not lines:
        return []
    
    headers = [h.strip() for h in lines[0].split(",")]
    records = []
    for line in lines[1:]:
        vals = [v.strip() for v in line.split(",")]
        if len(vals) == len(headers):
            records.append(dict(zip(headers, vals)))
    return records


def records_to_json(records: list[dict]) -> str:
    return json.dumps(records, ensure_ascii=False, indent=2, sort_keys=True)


def _parse_val(val: str):
    if not val:
        return val
    lower = val.lower()
    if lower in ("true", "yes"):
        return True
    if lower in ("false", "no"):
        return False
    try:
        return int(val)
    except ValueError:
        try:
            return float(val.replace(",", "."))
        except ValueError:
            return val


def parse_settings(lines: list[str]) -> dict:
    result = {}
    current_list_key = None

    for raw_line in lines:
        line = raw_line.split("#")[0].strip()
        if not line:
            continue

        if line.startswith("- "):
            if current_list_key is not None:
                result[current_list_key].append(_parse_val(line[2:].strip()))
        elif line.endswith(":"):
            current_list_key = line[:-1].strip()
            result[current_list_key] = []
        elif ":" in line:
            key, val = line.split(":", 1)
            result[key.strip()] = _parse_val(val.strip())
            current_list_key = None

    return result


def merge_by_key(rows: list[dict], extra: dict, key: str = "id") -> list[dict]:
    result = []
    for row in rows:
        new_row = dict(row)
        val = new_row.get(key)
        if val in extra:
            for k, v in extra[val].items():
                if k not in new_row:
                    new_row[k] = v
        result.append(new_row)
    return result
