import re

pattern = re.compile(r"-?\d+")

lines = [list(map(int, pattern.findall(line))) for line in open("input.txt")]

M = 4_000_000  # search boundary

for Y in range(M + 1):
    if Y % 100_000 == 0:
        print(Y)

    intervals = []  # all the points that can not exists

    for sx, sy, bx, by in lines:
        d = abs(sx - bx) + abs(sy - by)  # distance between the beacon and the sensor
        offset = d - abs(sy - Y)

        # This sensor pair does not give us any information
        if offset < 0:
            continue

        lx = sx - offset
        hx = sx + offset

        intervals.append((lx, hx))

    intervals.sort()  # sorted by first by lower bound and then upper bound

    q = []  # contains all non overlapping intervals -> combined into one itnerval (what isnt allowed)

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

    x = 0
    for lo, hi in q:
        if x < lo:  # none of the future intervals will intersect x
            print(x * 4_000_000 + Y)
            exit()
        else:
            x = hi + 1

        if x > M:  # if its out of our boundary
            break
