
from collections import defaultdict
def test():
    ex = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732"""

    run(ex)

visited = set()
visited_rating = defaultdict(int)
def run(input: str):
    grid = [[int(c) for c in l] for l in input.split("\n")]

    zeros = []
    for r, line in enumerate(grid):
        for c, col in enumerate(line):
            if col == 0:
                zeros.append((r,c))
    val = 0
    scores = []
    ratings = []
    for (row, col) in zeros:
        find_path(grid, row,col, val)
        scores.append(len(visited))
        ratings.append(sum(visited_rating.values()))
        
        visited.clear()
        visited_rating.clear()

    print("1: ", sum(scores))
    print("2: ", sum(ratings))

def find_path(grid, row, col, val):

    if val > 9:
        return False
    if (row < 0 or row >= len(grid)) or (col < 0 or col >= len(grid[0])):
        return False
    if grid[row][col] == val :
        if val == 9:
            visited.add((row, col))
            visited_rating[(row, col)] += 1
            return True
        else:
            return find_path(grid, row +1,col, val+1) + find_path(grid, row,col +1, val+1) + find_path(grid, row -1,col, val+1) + find_path(grid, row,col-1, val+1)
    return False
        
        