valid_levels = {"DEBUG", "INFO", "WARNING", "ERROR"}

def parse_event(line: str) -> dict:
    line = line.strip()
    if not line:
        raise ValueError("Пустая строка")
        
    parts = line.split(maxsplit=2)
    
    if len(parts) < 3:
        raise ValueError(f"Недостаточно полей в строке: '{line}'")
        
    time_str, level, message = parts
    
    if level not in valid_levels:
        raise ValueError(f"Неизвестный уровень лога: '{level}'")
        
    return {
        "time": time_str,
        "level": level,
        "message": message
    }

def count_levels(lines) -> dict:
    counts = {}
    for line in lines:
        if not line.strip():
            continue
            
        try:
            event = parse_event(line)
            level = event["level"]
            counts[level] = counts.get(level, 0) + 1
        except ValueError:
            counts["BROKEN"] = counts.get("BROKEN", 0) + 1
            
    return counts


def top_errors(lines, n: int) -> list:
    error_counts = {}
    
    for line in lines:
        if not line.strip():
            continue
        try:
            event = parse_event(line)
            if event["level"] == "ERROR":
                msg = event["message"]
                error_counts[msg] = error_counts.get(msg, 0) + 1
        except ValueError:
            continue
            
    items = [[msg, count] for msg, count in error_counts.items()]
    
    items.sort(key=lambda x: (-x[1], x[0]))
    
    return items[:n]


def format_report(counts, errors):
    pass
