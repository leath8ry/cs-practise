from pathlib import Path

def count_by_extension(paths: list[str]) -> dict[str, int]:
    counts = {}
    for p in paths:
        ext = Path(p).suffix.lower().lstrip(".")
        counts[ext] = counts.get(ext, 0) + 1
    return counts

def deepest_path(paths: list[str]) -> str:
    if not paths:
        return ""
    return sorted(paths, key=lambda x: (-x.count("/"), x))[0]

def human_size(n_bytes: int) -> str:
    units = ["Б", "КБ", "МБ", "ГБ", "ТБ"]
    
    size = float(n_bytes)
    unit_index = 0
    
    while size >= 1024 and unit_index < len(units) - 1:
        size /= 1024
        unit_index += 1
        
    if unit_index == 0:
        return f"{int(size)} {units[unit_index]}"
    else:
        return f"{size:.1f} {units[unit_index]}"
