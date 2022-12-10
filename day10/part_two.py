with open(file="input.txt", mode="r") as f:
    lines = f.read().strip().split("\n")


def check_cycle():
    global num_cycle, x_value, column
    if num_cycle in set(range(40, 241, 40)):
        print("\n")


def check_overlap():
    global x_value
    if abs(x_value - ((num_cycle - 1) % 40)) <= 1:
        print("#", end="")
    else:
        print(".", end="")


x_value = 1
num_cycle = 0
for line in lines:
    command, *value = line.split()
    if command == "noop":
        num_cycle += 1

        check_overlap()
        check_cycle()

    elif command == "addx":
        num_cycle += 1
        check_overlap()
        check_cycle()

        num_cycle += 1
        check_overlap()
        check_cycle()

        value = int(*value)
        x_value += value
