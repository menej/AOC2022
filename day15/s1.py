import re

pattern = re.compile(r"-?\d+")

cannot = set()  # x coordinates that the beacon can not be in
known = set()  # known beacons that are within the set

Y = 2_000_000

intervals = []  # all the points that can not exists

for line in open("input.txt"):
    sx, sy, bx, by = map(int, pattern.findall(line))

    d = abs(sx - bx) + abs(sy - by)  # distance between the beacon and the sensor
    offset = d - abs(sy - Y)

    # This sensor pair does not give us any information
    if offset < 0:
        continue

    lx = sx - offset
    hx = sx + offset

    intervals.append((lx, hx))

    if by == Y:
        known.add(bx)


intervals.sort()  # sorted by first by lower bound and then upper bound

q = []  # contains all non overlapping intervals -> combined into one itnerval

for lo, hi in intervals:
    if not q:
        q.append([lo, hi])
        continue

    qlo, qhi = q[-1]
    if lo > qhi + 1:  # there is no overlap, but can also barely touch
        q.append([lo, hi])
        continue

    # our new interval of the two combined is the lowest of the lows and the highest of the highs
    # lowest of the low is going to be qlo (because we sorted the intervals)
    q[-1][1] = max(qhi, hi)

cannot = set()

for lo, hi in q:
    for x in range(lo, hi + 1):
        cannot.add(x)

print(len(cannot - known))