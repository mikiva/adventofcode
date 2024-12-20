from collections import defaultdict, Counter
def test():
    ex = """###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############"""

    run(ex)


def run(input: str):
    grid = input.split("\n")
    grid = [[c for c in g] for g in grid]
    
    start = ()
    finish = ()

    for y, row in enumerate(grid):
        for x, col in enumerate(row):
            if col == "S":
                start = (x,y)
            elif col == "E":
                finish = (x,y)
    
    track = get_track(grid, start,finish)
    shortcuts = defaultdict(set)
    for idx, position in enumerate(track):
        x,y = position
        
        if (x-2,y) in track and (short := track.index((x-2,y))) > idx and grid[y][x-1] == "#":
            new_track = track[:idx] + track[short:]
            shortcuts[len(new_track)+1].add((x-1,y,x-2,y))
        
        if (x+2,y) in track and (short := track.index((x+2,y))) > idx  and grid[y][x+1] == "#":
            new_track = track[:idx] + track[short:]
            shortcuts[len(new_track)+1].add((x+1,y,x+2,y))
        
        if (x,y+2) in track and (short := track.index((x,y+2))) > idx and grid[y+1][x] == "#":
            new_track = track[:idx] + track[short:]
            shortcuts[len(new_track)+1].add((x,y+1,x,y+2))
        
        if (x,y-2) in track and (short := track.index((x,y-2))) > idx and grid[y-1][x] == "#":
            new_track = track[:idx] + track[short:]
            shortcuts[len(new_track)+1].add((x,y-1,x,y-2))

    
    shortcuts = sorted(shortcuts.items())
    found_shortcuts=0
    for key, value in shortcuts:
        if ((len(track) -1) - key) >= 100:
            found_shortcuts += len(value)
    
    print("1: ", found_shortcuts)


def get_track(grid, start, finish):
    steps = 0
    size = len(grid)

    queue = []
    queue.append(start)
    visited = set([start])
    path_from = {}
    while queue:
        path = queue.pop(0)
        x,y = path
        
        if x > 0 and x < size and grid[y][x-1] in ["E","."] and (x-1, y) not in visited:
            queue.append((x-1, y))
            visited.add((x-1,y))
            path_from[(x-1, y)] = (x,y)
        if x < size - 1 and grid[y][x+1] in ["E","."] and (x+1, y) not in visited:
            queue.append((x+1, y))
            visited.add((x+1,y))
            path_from[(x+1, y)] = (x,y)
        if y < size -1 and grid[y+1][x] in ["E","."] and (x, y+1) not in visited:
            queue.append((x, y+1))
            visited.add((x,y+1))
            path_from[(x, y+1)] = (x,y)
        if y > 0 and grid[y-1][x] in ["E","."] and (x, y-1) not in visited:
            queue.append((x, y-1))
            visited.add((x,y-1))
            path_from[(x, y-1)] = (x,y)

    position = finish
    steps = [position]
    while position != start:
        position = path_from[position]
        x,y = position
        steps.append(position)

    return list(reversed(steps))