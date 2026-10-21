def parse_record(line):
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


def read_valid(lines):
    pass

def average_by_city(records):
    pass

def warmest_city(records):
    pass
