with open("input.txt") as f:
    lines = f.read().strip().split("\n")

obstacles = set()
num_sand = 0

min_x = -1
max_x = -1
min_y = -1
max_y = -1

# FInding min_x and max_x and min_y and max_y
for line in lines:
    line = list(map(str.strip, line.split("->")))
    for rock in line:
        x, y = tuple(map(int, rock.split(",")))
        if x > max_x:
            max_x = x
        if x < min_x or min_x == -1:
            min_x = x
        if y > max_y:
            max_y = y
        if y < min_y or min_y == -1:
            min_y = y

# Create rocks
for line in lines:
    line = list(map(str.strip, line.split("->")))
    for rock_before, rock_after in zip(line[0::], line[1::]):
        x1, y1 = tuple(map(int, rock_before.split(",")))
        x2, y2 = tuple(map(int, rock_after.split(",")))
        if x1 != x2:
            for some_rock_x in range(min(x1, x2), max(x1, x2) + 1):
                obstacles.add((some_rock_x, y1))
        elif y1 != y2:
            for some_rock_y in range(min(y1, y2), max(y1, y2) + 1):
                obstacles.add((x1, some_rock_y))
        else:
            raise RuntimeError("Something wrong.")

sand_starting_point = (500, 0)
current_sand_coords = sand_starting_point
is_hit = False


def go_down(sand_coords):
    return sand_coords[0], sand_coords[1] + 1


def go_left_down(sand_coords):
    return sand_coords[0] - 1, sand_coords[1] + 1


def go_right_down(sand_coords):
    return sand_coords[0] + 1, sand_coords[1] + 1


# Going to run infinitely (something has to be fixed in the while conditional clause)
while min_x <= current_sand_coords[0] <= max_x:
    if go_down(current_sand_coords) not in obstacles:
        current_sand_coords = go_down(current_sand_coords)
        continue
    elif go_left_down(current_sand_coords) not in obstacles:
        current_sand_coords = go_left_down(current_sand_coords)
        continue
    elif go_right_down(current_sand_coords) not in obstacles:
        current_sand_coords = go_right_down(current_sand_coords)
        continue
    else:
        obstacles.add(current_sand_coords)
        num_sand += 1
        current_sand_coords = sand_starting_point
        print(num_sand)
