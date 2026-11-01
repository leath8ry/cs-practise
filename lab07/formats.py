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

