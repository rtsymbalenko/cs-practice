import os


def count_by_extension(paths: list[str]) -> dict[str, int]:
    counts = {}
    for path in paths:
        name = path.split("/")[-1]
        ext = os.path.splitext(name)[1][1:].lower()
        counts[ext] = counts.get(ext, 0) + 1
    return counts


def deepest_path(paths: list[str]) -> str:
    if not paths:
        return ""
    
    best = paths[0]
    for path in paths:
        slashes = path.count("/")
        best_slashes = best.count("/")
        
        if slashes > best_slashes:
            best = path
        elif slashes == best_slashes and path < best:
            best = path
            
    return best


def human_size(n_bytes: int) -> str:
    if n_bytes < 1024:
        return f"{n_bytes} Б"
    units = ["КБ", "МБ", "ГБ", "ТБ"]
    size = float(n_bytes)
    for unit in units:
        size /= 1024
        if size < 1024 or unit == "ТБ":
            return f"{size:.1f} {unit}"
