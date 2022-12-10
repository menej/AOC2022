with open("input.txt") as f:
    moves = f.read().strip().split("\n")

hx, hy = 0, 0
tx, ty = 0, 0


def touching(x1, x2, y1, y2):
    return abs(x1 - x2) <= 1 and abs(y1 - y2) <= 1


def move_node(dx, dy):
    global hx, hy, tx, ty

    hx += dx
    hy += dy

    if not touching(hx, hy, tx, ty):
        sign_x = 0 if hx == tx else (hx - tx) / abs(hx - tx)
        sign_y = 0 if hy == ty else (hy - ty) / abs(hy - ty)

        tx += sign_x
        ty += sign_y


dd = {
    "R": [1, 0],
    "U": [0, 1],
    "L": [-1, 0],
    "D": [0, -1]
}

tail_visited = set()
tail_visited.add((tx, ty))

for move in moves:
    operation, amount = move.split(" ")
    amount = int(amount)

    dx, dy = dd[operation]
    for _ in range(amount):
        move_node(dx, dy)
        tail_visited.add((tx, ty))

print(len(tail_visited))