import json  

def csv_to_records(text: str) -> list[dict]:
    if not text.strip():
        return []
    lines = text.strip().splitlines()
    headers = [h.strip() for h in lines[0].split(",")]
    records = []
    for line in lines[1:]:
        if not line.strip():
            continue
        values = [v.strip() for v in line.split(",")]
        record = {}
        for i, header in enumerate(headers):
            if i < len(values):
                record[header] = values[i]
            else:
                record[header] = ""
        records.append(record)
    return records

def _convert_value(val_str: str):
    val = val_str.strip()
    if not val:
        return None
        
    lower_val = val.lower()
    if lower_val in ("true", "yes"):
        return True
    if lower_val in ("false", "no"):
        return False
    
    try:
        if "." not in val and "," not in val:
            return int(val)
    except ValueError:
        pass
        
    try:
        return float(val.replace(",", "."))
    except ValueError:
        return val

def parse_settings(lines: list[str]) -> dict:
    result = {}
    current_list_key = None
    
    for line in lines:
        comment_idx = line.find("#")
        if comment_idx != -1:
            line = line[:comment_idx]
            
        stripped = line.strip()
        if not stripped:
            continue
            
        if stripped.startswith("- ") and current_list_key is not None:
            item_val = stripped[2:].strip()
            converted = _convert_value(item_val)
            if converted is not None:
                result[current_list_key].append(converted)
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
        new_row = dict(row)
        
        if row_key in extra:
            for k, v in extra[row_key].items():
                if k not in new_row:
                    new_row[k] = v
                    
        merged.append(new_row)
    return merged

def records_to_json(records: list[dict]) -> str:
    return json.dumps(
        records, 
        ensure_ascii=False, 
        indent=2, 
        sort_keys=True
    )
