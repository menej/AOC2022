grid = [list(x) for x in open("input.txt").read().strip().splitlines()]

for r, row in enumerate(grid):
    for c, item in enumerate(row):
        if item == "S":
            sr = r
            sc = c
            grid[r][c] = "a"
        if item == "E":
            er = r
            ec = c
            grid[r][c] = "z"

queue = []
queue.append((0, sr, sc))
visited = {(sr, sc)}

while queue:
    distance, row, column = queue.pop(0)
    for next_row, next_column in [(row + 1, column), (row - 1, column), (row, column + 1), (row, column - 1)]:
        # If its not valid
        if next_row < 0 or next_column < 0 or next_row >= len(grid) or next_column >= len(grid[0]):
            continue
        # If we already visited the node
        if (next_row, next_column) in visited:
            continue
        # If the elevation is greater than 1
        if ord(grid[next_row][next_column]) - ord(grid[row][column]) > 1:
            continue
        if next_row == er and next_column == ec:
            print(distance + 1)
            exit(0)
        visited.add((next_row, next_column))
        queue.append((distance + 1, next_row, next_column))
