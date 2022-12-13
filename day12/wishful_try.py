with open("input.txt") as f:
    lines = f.read().split("\n")

visited = set()
positions = {}

# Naredim preslikavo posameznih elementov
starting_position = None
x_pos = 0
y_pos = 0
for line in lines:
    row = list(line)
    for element in row:
        element_pos = (x_pos, y_pos)
        positions[element_pos] = element
        x_pos += 1
        if element == 'S':
            starting_position = element_pos
    x_pos = 0
    y_pos += 1

starting_path = [('S', starting_position)]
queue = [(0, starting_position)]
found_shortest = False
shortest_path = None


def get_elevation(coord):
    el = positions[coord]
    if el == 'S':
        el = 'a'
    if el == 'E':
        el = 'z'
    return ord(el)


while queue:
    cost, coord = queue.pop(0)

    if positions[coord] == 'E':
        print(cost)
        break

    for dx, dy in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
        new_coord = (coord[0] + dx, coord[1] + dy)
        if new_coord in visited:
            continue
        if new_coord not in positions:
            continue

        neighbour_coordinates = new_coord

        if get_elevation(new_coord) - get_elevation(coord) > 1:
            continue

        visited.add(new_coord)
        queue.append((cost + 1, new_coord))
