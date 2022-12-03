with open("input.txt") as f:
    lines = f.readlines()

prioritiesSum = 0

for line in lines:
    line = line.strip()
    firstCompartment = line[:int(len(line) / 2)]
    secondCompartment = line[int(len(line) / 2):]

    bothContain = None

    for element in firstCompartment:
        if element in secondCompartment:
            bothContain = element
            break
    else:
        raise EOFError("Invalid Data")

    elementPriority = 0

    if bothContain.isupper():
        elementPriority = ord(bothContain) - ord('A') + 25 + 2
    elif bothContain.islower():
        elementPriority = ord(bothContain) - ord('a') + 1
    else:
        raise RuntimeError

    prioritiesSum += elementPriority

print(prioritiesSum)

