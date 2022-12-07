with open("input.txt") as f:
    lines = f.readlines()

prioritiesSum = 0

for group in zip(lines[::3], lines[1::3], lines[2::3]):
    firstElf = set(group[0].strip())
    secondElf = set(group[1].strip())
    thirdElf = set(group[2].strip())

    badge = (firstElf & secondElf & thirdElf).pop()

    elementPriority = 0

    if badge.isupper():
        elementPriority = ord(badge) - ord('A') + 25 + 2
    elif badge.islower():
        elementPriority = ord(badge) - ord('a') + 1
    else:
        raise RuntimeError

    prioritiesSum += elementPriority


print(prioritiesSum)

