import json


def csv_to_records(text: str) -> list[dict]:
    if not text or not text.strip():
        return []
    lines = text.strip().splitlines()
    headers = [h.strip() for h in lines[0].split(",")]
    records = []
    for line in lines[1:]:
        if not line.strip():
            continue
        values = [v.strip() for v in line.split(",")]
        record = {
            header: (values[i] if i < len(values) else "")
            for i, header in enumerate(headers)
        }
        records.append(record)
    return records


def _convert_value(val_str: str):
    val = val_str.strip()
    if not val:
        return ""

    lower_val = val.lower()
    if lower_val in ("true", "yes"):
        return True
    if lower_val in ("false", "no"):
        return False

    if "." not in val and "," not in val:
        try:
            return int(val)
        except ValueError:
            pass

    normalized = val.replace(",", ".")
    if "." in normalized and lower_val not in ("inf", "-inf", "+inf", "nan"):
        try:
            return float(normalized)
        except ValueError:
            pass

    return val


def parse_settings(lines: list[str]) -> dict:
    result = {}
    current_list_key = None

    for raw_line in lines:
        comment_pos = raw_line.find("#")
        if comment_pos != -1:
            raw_line = raw_line[:comment_pos]

        stripped = raw_line.strip()
        if not stripped:
            continue

        if stripped.startswith("-") and current_list_key is not None:
            item_val = stripped[1:].strip()
            if item_val:
                result[current_list_key].append(_convert_value(item_val))
            continue

        if ":" in stripped:
            key, _, val_str = stripped.partition(":")
            key = key.strip()
            val_str = val_str.strip()

            if not val_str:
                result[key] = []
                current_list_key = key
            else:
                result[key] = _convert_value(val_str)
                current_list_key = None

    return result


def merge_by_key(rows: list[dict], extra: dict, key: str = "id") -> list[dict]:
    merged = []
    for row in rows:
        row_key = row.get(key)
        if row_key in extra and isinstance(extra[row_key], dict):
            new_row = {**extra[row_key], **row}
        else:
            new_row = dict(row)
        merged.append(new_row)
    return merged


def records_to_json(records: list[dict]) -> str:
    return json.dumps(
        records,
        ensure_ascii=False,
        indent=2,
        sort_keys=True
    )
