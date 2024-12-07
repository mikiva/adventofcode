
from collections import defaultdict
from math import ceil

def test():
    ex = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""

    run(ex)


visited = set()

def run(input):
    grid = [ [s for s in r] for r in [inp for inp in input.split("\n")]]

    #Start
    direction = "^"
    (r,c) = find_current_location(grid, direction)
    max_count = 100
    count = 0
    while_count = 0
    while while_count < 100000000:
        (r,c), new_direction = make_move(grid, (r,c), direction)
        
        if (r < 0 or r >= len(grid)) or (c < 0 or c >= len(grid[0])):
            print("outside", count, len(visited))
            break
        if new_direction == direction:
            count += 1
            visited.add((r,c))

        direction = new_direction
        while_count += 1


def find_current_location(grid, to_find):
    
    for r, row in  enumerate(grid):
        for c, col in enumerate(row):
            if col == to_find:
                return (r,c)

    return (-1, -1)

    ...


next_direction = {"^": ">", ">": "v", "v": "<", "<": "^"}

def make_move(grid, position, direction):
    (r,c) = position




    match direction:
        case "^":
            if r-1 >= 0 and grid[r-1][c] == "#":
                return (r,c), next_direction[direction]
            else:
                return (r-1, c), direction


        case ">":
            if c+1 < len(grid[r]) and  grid[r][c+1] == "#":
                return (r,c), next_direction[direction]
            else:
                return (r, c+1), direction
            ...
        case "v":
            if r+1 < len(grid) and grid[r+1][c] == "#":
                return (r,c), next_direction[direction]
            else:
                return (r+1, c), direction
            ...
        case "<":
            if c-1 >= 0 and grid[r][c-1] == "#":
                return (r,c), next_direction[direction]
            else:
                return (r, c-1), direction
            ...



#    return position, direction