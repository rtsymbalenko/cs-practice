def sum(x: float, y: float) -> float:
    return x + y

def sub(x: float, y: float) -> float:
    return x - y

a: float = float(input())
b: float = float(input())

print(f"sum: {sum(a, b)}")
print(f"sub: {sub(a, b)}")
