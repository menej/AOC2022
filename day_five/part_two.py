with open("input.txt", mode="r") as f:
    lines = f.readlines()

# Reading all the stack inputs
stack_inputs = []
line_counter = 0
for line in lines:
    line_counter += 1
    line = line.rstrip()
    if line == "":
        break
    stack_inputs.append(line)

# Creating my stack collection
num_stacks = int(stack_inputs.pop()[-1])
stack_collection = [list() for _ in range(num_stacks)]

# Filling all thes tacks from stack collection
for line in stack_inputs[::-1]:
    stack_counter = 0
    for element in line[1::4]:
        if element != " ":
            stack_collection[stack_counter].append(element)
        stack_counter += 1

# Processing all the instructions from the command inputs
for line in lines[line_counter:]:
    instruction = line.rstrip().split(" ")

    num_moves = int(instruction[1])
    from_stack = int(instruction[3]) - 1
    to_stack = int(instruction[5]) - 1

    moving_stack = []
    for _ in range(num_moves):
        element = stack_collection[from_stack].pop()
        moving_stack.append(element)

    for _ in range(num_moves):
        element = moving_stack.pop()
        stack_collection[to_stack].append(element)

# Building the output string
output_string = ""
for stack in stack_collection:
    output_string += stack[-1]

print(output_string)