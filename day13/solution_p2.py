import functools


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


# We only need to compare each item against our divider keys
x = list(map(eval, open("input.txt").read().split()))

i2 = 1
i6 = 2

for a in x:
    # Because i2 and i6 are transative we can only check once
    if f(a, [[2]]) < 0:
        i2 += 1
        i6 += 1
    elif f(a, [[6]]) < 0:
        i6 += 1

print(i2 * i6)

# Or we can do something like this
x = list(map(eval, open("input.txt").read().split())) + [[[2]], [[6]]]
# cmp_to_key takes a comparator function and turns it into a key function
x.sort(key=functools.cmp_to_key(f))
print((x.index([[2]]) + 1) * (x.index([[6]]) + 1))