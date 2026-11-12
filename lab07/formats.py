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
