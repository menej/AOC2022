with open(file="input.txt", mode="r") as f:
    lines = f.readlines()

trees = []

for i in range(len(lines)):
    trees.append(list())
    row = lines[i].strip()
    for tree in row:
        trees[i].append(int(tree))

highest_scenic = 0
for i in range(len(trees[0])):
    for j in range(len(trees)):
        scenic_score = 1

        tree_value = int(trees[i][j])

        # Check upper neighbors
        count_upper = 0
        for x in range(i - 1, -1, -1):
            up_tree = trees[x][j]
            count_upper += 1
            if up_tree >= tree_value:
                break

        # Check bottom neighbors
        count_lower = 0
        for x in range(i + 1, len(trees[0])):
            down_tree = trees[x][j]
            count_lower += 1
            if down_tree >= tree_value:
                break

        # Check left neighbors
        count_lefties = 0
        for x in range(j - 1, -1, -1):
            left_tree = trees[i][x]
            count_lefties += 1
            if left_tree >= tree_value:
                break

        # Check right neighbors
        count_righties = 0
        for x in range(j + 1, len(trees)):
            right_tree = trees[i][x]
            count_righties += 1
            if right_tree >= tree_value:
                break

        scenic_score = count_upper * count_lower * count_lefties * count_righties

        if scenic_score > highest_scenic:
            highest_scenic = scenic_score

print(highest_scenic)
