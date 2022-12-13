import json


def checking(left_list, right_list, trigger):
    if len(left_list) == 0 and len(right_list) == 0 and trigger:
        return None
    if len(left_list) == 0:
        return True
    if len(right_list) == 0:
        return False
    if len(left_list) == 1 and not isinstance(left_list, list):
        left_list = list(left_list)
    if len(right_list) == 1 and not isinstance(right_list, list):
        right_list = list(right_list)

    left_element = left_list.pop(0)
    right_element = right_list.pop(0)

    if isinstance(left_element, list) and not isinstance(right_element, list):
        right_element = [right_element]
    elif not isinstance(left_element, list) and isinstance(right_element, list):
        left_element = [left_element]

    if isinstance(left_element, list) and isinstance(right_element, list):
        value = checking(left_element, right_element, True)
        if value is not None:
            return value

    if isinstance(left_element, int) and isinstance(right_element, int):
        if left_element > right_element:
            return False
        elif left_element < right_element:
            return True

    return checking(left_list, right_list, trigger)


with open("input.txt", "r") as f:
    lines = list(filter(lambda a: a != "", f.read().strip().split("\n")))

lines.append("[[2]]")
lines.append("[[6]]")
lines.append("[[3]]")

sum_indices = 0
right_order = False
xs = []

for step in range(len(lines) - 1):
    min_idx = step

    for j in range(step + 1, len(lines)):
        a = lines[min_idx]
        b = lines[j]
        if checking(json.loads(lines[j]), json.loads(lines[min_idx]), False):
            min_idx = j
    lines[step], lines[min_idx] = lines[min_idx], lines[step]

oke = 1
for index, line in enumerate(lines):
    if line == "[[2]]" or line == "[[6]]":
        oke *= (index + 1)

print(oke)
