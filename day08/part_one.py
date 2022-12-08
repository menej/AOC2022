with open(file="input.txt", mode="r") as f:
    lines = f.readlines()

trees = []

for i in range(len(lines)):
    trees.append(list())
    row = lines[i].strip()
    for tree in row:
        trees[i].append(int(tree))

count_visable = 0
for i in range(len(trees[0])):
    for j in range(len(trees)):

        if i == 0 or j == 0 or i >= len(trees[0]) - 1 or j >= len(trees) - 1:
            count_visable += 1
            continue

        tree_value = int(trees[i][j])

        # Check upper -> lower i til 0
        checking_trees = []
        for x in range(0, i):
            checking_trees.append(trees[x][j])
        checked_trees = list(filter(lambda checking_tree: checking_tree < tree_value, checking_trees))
        if len(checked_trees) == len(checking_trees):
            count_visable += 1
            continue

        # Check lower -> raise i til len(trees[0]) - 1
        checking_trees = []
        for x in range(i + 1, len(trees[0])):
            checking_trees.append(trees[x][j])
        checked_trees = list(filter(lambda checking_tree: checking_tree < tree_value, checking_trees))
        if len(checked_trees) == len(checking_trees):
            count_visable += 1
            continue

        # Check lefties -> lower j til 0
        checking_trees = []
        for x in range(0, j):
            checking_trees.append(trees[i][x])
        checked_trees = list(filter(lambda checking_tree: checking_tree < tree_value, checking_trees))
        if len(checked_trees) == len(checking_trees):
            count_visable += 1
            continue

        # Check righties -> raise j til len(trees) - 1
        checking_trees = []
        for x in range(j + 1, len(trees)):
            checking_trees.append(trees[i][x])
        checked_trees = list(filter(lambda checking_tree: checking_tree < tree_value, checking_trees))
        if len(checked_trees) == len(checking_trees):
            count_visable += 1
            continue

print(count_visable)
