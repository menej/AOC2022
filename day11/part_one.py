class Monkey:
    WORRY_DECREASE = 3

    def __init__(self, monkey_number: int, items: list, operation: tuple, test: int, test_true: int, test_false: int):
        self.monkey_number = monkey_number
        self.items = items
        self.operation = operation
        self.test = test
        self.test_true = test_true
        self.test_false = test_false
        self.count_inspections = 0

    def inspect(self):
        current_item = self.items.pop(0)
        self.count_inspections += 1

        current_item = self.increase_worry(current_item)
        current_item = self.decrease_worry(current_item)
        return self.test_item(current_item), current_item

    def decrease_worry(self, item):
        return item // self.WORRY_DECREASE

    def increase_worry(self, item):
        operator = self.operation[0]
        worry_change = self.operation[1]
        if operator == "*":
            if worry_change == "old":
                return item * item
            return item * int(worry_change)
        if operator == "+":
            if worry_change == "old":
                return item + item
            return item + int(worry_change)
        raise RuntimeError("Operation unknown: " + operator)

    def test_item(self, item):
        if item % self.test == 0:
            return self.test_true
        else:
            return self.test_false


with open("input.txt") as f:
    lines = f.read().split("\n")

# Create monkeys
monkeys = []
index = 0
while index < len(lines):
    line = lines[index]
    monkey_number = int(line.split(" ")[1].replace(":", ""))
    monkey_info = [monkey_number]
    while not line.startswith("If false"):
        index += 1
        line = lines[index].strip()
        if line.startswith("Starting items"):
            items = line.split(":")[1].strip()
            items = list(map(int, items.split(", ")))
            monkey_info.append(items)
        elif line.startswith("Operation"):
            operation = line.split("= old")[1].strip()
            operation = tuple(operation.split(" "))
            monkey_info.append(operation)
        elif line.startswith("Test"):
            test = int(line.split("divisible by")[1].strip())
            monkey_info.append(test)
        elif line.startswith("If true") or line.startswith("If false"):
            test_result = int(line.split("monkey")[1].strip())
            monkey_info.append(test_result)
    monkey = Monkey(*monkey_info)
    monkeys.append(monkey)
    index += 2


# Play 20 rounds of this

for _ in range(10000):
    for monkey in monkeys:
        if len(monkey.items) == 0:
            continue
        for _ in range(len(monkey.items)):
            partner_number, item = monkey.inspect()
            monkeys[partner_number].items.append(item)

monkey_inspections = set()
for monkey in monkeys:
    monkey_inspections.add(monkey.count_inspections)

first_largest = max(monkey_inspections)
monkey_inspections.remove(first_largest)
second_largest = max(monkey_inspections)
monkey_inspections.remove(second_largest)
print(first_largest * second_largest)

