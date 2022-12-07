from collections import defaultdict

with open(file="input.txt", mode="r") as f:
    lines = f.readlines()

dir_contains = defaultdict(list)
files_contains = defaultdict(list)
file_sizes = defaultdict(int)
current_directory = ""

file_index = 0

while file_index < len(lines):
    command_line = lines[file_index].rstrip().split(" ")
    if command_line[0] == "$":
        command = command_line

        if command[1] == "ls":
            file_index += 1
            command_line = lines[file_index].rstrip().split()

            while command_line[0] != "$" and file_index < len(lines):
                file_type, file_name = command_line

                full_file_path = current_directory
                if full_file_path != "/":
                    full_file_path += "/"
                full_file_path += file_name
                full_file_path.replace("//", "/")

                if file_type == "dir":
                    dir_contains[current_directory].append(full_file_path)
                    dir_contains[full_file_path] = []  # Because it is a directory just create it inside
                elif file_type.isnumeric():
                    file_sizes[full_file_path] = int(file_type)
                    files_contains[current_directory].append(full_file_path)
                else:
                    raise RuntimeError("File of this type does not exists. File type: " + file_type)
                file_index += 1
                if file_index < len(lines):
                    command_line = lines[file_index].rstrip().split()
            else:
                file_index -= 1

        elif command[1] == "cd":
            if command[2] == "..":
                current_directory = "/".join(current_directory.split("/")[:-1])
            else:
                if command[2] != "/" and current_directory != "/":
                    current_directory += "/"
                current_directory += command[2]
                current_directory.replace("//", "/")
        else:
            raise RuntimeError("File of this type does not exists. File type: " + command_line[0])

    file_index += 1

print(dir_contains)
print(files_contains)
print(file_sizes)

direct_sizes = defaultdict(int)
# Get direct size of each directory
for directory, files in files_contains.items():
    for file in files:
        direct_sizes[directory] += int(file_sizes[file])


def get_directory_size(x):
    if x not in dir_contains:
        return direct_sizes[x]
    total = 0
    for y in dir_contains[x]:
        total += get_directory_size(y)
    return direct_sizes[x] + total


# Check real sizes of each directory
needed_space = 30000000
total_space = 70000000
space_unavailable = get_directory_size("/")

minimum_directory = None
minimum_directory_size = None

for directory, directories in dir_contains.items():
    if directory == "/":
        continue
    total_size = get_directory_size(directory)

    difference_current = total_space - space_unavailable + total_size

    if minimum_directory is None and difference_current > needed_space:
        minimum_directory = directory
        minimum_directory_size = total_size
        continue

    if difference_current > needed_space:
        difference_previous = total_space - space_unavailable + minimum_directory_size
        if difference_current < difference_previous:
            minimum_directory_size = total_size
            minimum_directory = directory

print(minimum_directory)
print(minimum_directory_size)
