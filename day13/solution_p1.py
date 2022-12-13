with open("input.txt") as f:
    x = list(map(str.splitlines, f.read().strip().split("\n\n")))


def f(x, y):
    if isinstance(x, int):
        if isinstance(y, int):
            return x - y
        else:
            return f([x], y)
    else:
        if isinstance(y, int):
            return f(x, [y])

    for a, b in zip(x, y):
        v = f(a, b)
        if v:
            return v

    return len(x) - len(y)


t = 0
for i, (a, b) in enumerate(x):
    if f(eval(a), eval(b)) < 0:
        t += i + 1

print(t)
