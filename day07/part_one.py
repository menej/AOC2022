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

dir_sizes = defaultdict(int)
# Get direct size of each directory
for directory, files in files_contains.items():
    for file in files:
        dir_sizes[directory] += int(file_sizes[file])


def get_directory_size(x):
    if x not in dir_contains:
        return dir_sizes[x]
    total = 0
    for y in dir_contains[x]:
        total += get_directory_size(y)
    return dir_sizes[x] + total


sizes_match = []
# Check real sizes of each directory
for directory, directories in dir_contains.items():
    total_size = get_directory_size(directory)

    if total_size < 100000:
        sizes_match.append(total_size)

print(sum(sizes_match))
