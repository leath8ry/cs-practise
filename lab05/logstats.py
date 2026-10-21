valid_levels = {"DEBUG", "INFO", "WARNING", "ERROR"}

def parse_event(line):
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

def count_levels(lines):
    pass

def top_errors(lines, n):
    pass

def format_report(counts, errors):
    pass
