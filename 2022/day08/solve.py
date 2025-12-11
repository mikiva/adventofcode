import os
from collections import defaultdict
from time import time

f = f"../inputs/{os.path.split(os.getcwd())[1]}.txt"
input_lines = [[dict(h=int(t), visits=0) for t in tree_line] for tree_line in open(f).read().split("\n")]


def rotate(grid):
    return list([l for l in zip(*grid[::-1])])

lines = input_lines
for _ in range(4):
    for row in lines:
        height = -1
        for col in row:
            if (h := col.get("h")) > height:
                height = h
                col["visits"] += 1

    lines = rotate(lines)

visits = 0
v = sum([len([c for c in row if c["visits"] > 0]) for row in lines])
print("p1", v)

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # RIGHT, DOWN, LEFT, UP
candidates = []
for i, row in enumerate(lines):
    for j, col in enumerate(row):
        col['coors'] = (i, j)
        candidates.append(col)

wi, wj = len(lines) - 1, len(lines[0]) - 1

highest = 1
scores = []
for candidate in candidates:
    score = 1
    cheight = candidate["h"]
    for x, y in directions:
        dir_score = 0
        # for i,j in candidate["coors"]:
        ni, nj = candidate["coors"]

        while True:
            ni, nj = (ni + x, nj + y)
            if ni < 0 or nj < 0 or ni > wi or nj > wj:
                break
            if cheight <= lines[ni][nj]["h"]:
                dir_score += 1
                break

            dir_score += 1

        score *= dir_score
    scores.append(score)
print("p2", max(scores))
print("=======")
