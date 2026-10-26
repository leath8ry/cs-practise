from pathlib import Path

def count_by_extension(paths: list[str]) -> dict[str, int]:
    counts = {}
    for p in paths:
        ext = Path(p).suffix.lower().lstrip(".")
        counts[ext] = counts.get(ext, 0) + 1
    return counts

