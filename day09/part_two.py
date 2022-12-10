with open("input.txt") as f:
    moves = f.read().strip().split("\n")

knots = [[0, 0] for _ in range(10)]


def touching(x1, y1, x2, y2):
    return abs(x1 - x2) <= 1 and abs(y1 - y2) <= 1


def move_node(dx, dy):
    global knots
    knots[0][0] += dx
    knots[0][1] += dy

    for i in range(1, 10):
        hx, hy = knots[i - 1]
        tx, ty = knots[i]

        if not touching(hx, hy, tx, ty):
            sign_x = 0 if hx == tx else (hx - tx) / abs(hx - tx)
            sign_y = 0 if hy == ty else (hy - ty) / abs(hy - ty)

            tx += sign_x
            ty += sign_y

        knots[i] = [tx, ty]


dd = {
    "R": [1, 0],
    "U": [0, 1],
    "L": [-1, 0],
    "D": [0, -1]
}

tail_visited = set()
tail_visited.add(tuple(knots[-1]))

for move in moves:
    operator, amount = move.split(" ")
    amount = int(amount)
    dx, dy = dd[operator]

    for _ in range(amount):
        move_node(dx, dy)
        tail_visited.add(tuple(knots[-1]))

print(len(tail_visited))
