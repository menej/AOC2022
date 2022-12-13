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
    lines = f.read().strip().split("\n")

sum_indices = 0
right_order = False

for index, [left, right] in enumerate(zip(lines[0::3], lines[1::3])):
    left = json.loads(left)
    right = json.loads(right)

    right_order = checking(left, right, False)
    if right_order:
        sum_indices += index + 1
print(sum_indices)
