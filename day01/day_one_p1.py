elvesInventories = {}

with open(file="input", mode="r") as f:
    lines = f.readlines()

currentIndex = 0

for line in lines:
    if line == "\n":
        currentIndex += 1
        continue

    calories = int(line.strip())

    elvesInventories.setdefault(currentIndex, 0)
    elvesInventories[currentIndex] += calories

toughestElf = max(elvesInventories, key=elvesInventories.get)
print(f"Elf {toughestElf} carried {elvesInventories[toughestElf]}")