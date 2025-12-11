
tree_map = []
count = 0

with open("input.txt", "r") as inp:
    x = 0
    for line in inp:
        row = line.strip("\n")
        if row[x % len(row)] == "#":
            count = count + 1
        x += 3
        tree_map.append(row)

slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
slope_trees = 1
for slope in slopes:
    c, x, y = 0, 0, 0
    while y < len(tree_map):
        row = tree_map[y]
        if row[x % len(row)] == "#":
            c += 1
        x += slope[0]
        y += slope[1]
    slope_trees = slope_trees * c

print("a", count)
print("b", slope_trees)
