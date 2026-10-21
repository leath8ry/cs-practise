def parse_record(line: str) -> dict:
    parts = line.split(";")
    if len(parts) != 3:
        raise ValueError(f"Неверное количество полей в строке: '{line}'")
    city, temp_str, date = parts
    if not city.strip() or not date.strip():
        raise ValueError(f"Город или дата пусты в строке: '{line}'")
    try:
        temp = float(temp_str)
    except ValueError:
        raise ValueError(f"Температура не является числом: '{temp_str}' в строке: '{line}'")
    return {"city": city.strip(), "temp": temp, "date": date.strip()}


def read_valid(lines: list[str]) -> list[dict]: 
    valid_records = []
    for line in lines:
        if not line.strip():
            continue
        try:
            record = parse_record(line)
            valid_records.append(record)
        except ValueError:
            continue
    return valid_records


def average_by_city(records: list[dict]) -> dict:
    totals = {}
    counts = {}
    for rec in records:
        city = rec["city"]
        temp = rec["temp"]
        
        totals[city] = totals.get(city, 0) + temp
        counts[city] = counts.get(city, 0) + 1
    averages = {}
    for city in totals:
        avg = totals[city] / counts[city]
        averages[city] = round(avg, 1) 
    return averages


def warmest_city(records: list[dict]) -> str:
    if not records:
        return ""  
    avgs = average_by_city(records)
    if not avgs:
        return ""
    best_city = sorted(avgs.keys(), key=lambda city: (-avgs[city], city))[0]
    return best_city
