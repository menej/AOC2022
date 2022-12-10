with open(file="input.txt", mode="r") as f:
    lines = f.read().strip().split("\n")


def check_cycle():
    global num_cycle, signal_strength, x_value
    if num_cycle in set(range(20, 221, 40)):
        signal_strength += (x_value * num_cycle)


signal_strength = 0
x_value = 1
num_cycle = 0

for line in lines:
    command, *value = line.split()
    if command == "noop":
        num_cycle += 1
        check_cycle()
    elif command == "addx":
        num_cycle += 1
        check_cycle()
        num_cycle += 1
        check_cycle()

        value = int(*value)
        x_value += value

print(signal_strength)
