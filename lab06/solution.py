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
