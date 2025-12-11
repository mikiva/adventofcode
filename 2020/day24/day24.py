from copy import deepcopy
def get_input(filename):
    lines = []
    with open(filename) as inp:
        lines =[x.strip("\n") for x in inp.readlines()]
    return lines

def parse_line(line):
    steps = []
    idx = 0
    while idx < len(line):
        step = ""
        if line[idx] in ["n", "s"]:
            step = line[idx] + line[idx+1]
            idx += 2
        else:
            step = line[idx]
            idx += 1
        
        steps.append(step)
    return steps


dirs =  {
    "ne": (1,-1),
    "e" :  (1,0),
    "nw": (0,-1),
    "w": (-1,0),
    "se": (0,1),
    "sw" : (-1,1)
}

def hex_grid(grid):


    x,y = 0,0
    for g in grid:
        tx, ty = dirs[g]
        x += tx
        y += ty

    return x,y



            

def get_black_tiles(tile_steps):

    black_tiles = set()
    for line in tile_steps:
        tile = hex_grid(line)
        if tile in black_tiles:
            black_tiles.remove(tile)
        else:
            black_tiles.add(tile)

    return black_tiles


def get_neighbors(tile):
    neighbors = []
    for d in dirs:
        cx, cy = dirs[d]
        n = (tile[0] + cx, tile[1] + cy)
        neighbors.append(n)

    return neighbors

def count_black_neighbors(tile, black):
    neigbor_count = 0
    for n in get_neighbors(tile):
        if n in black:
            neigbor_count += 1
    return neigbor_count

def run_day(tiles):
    stack = set()
    seen = set()
    new_tiles = deepcopy(tiles)

    for tile in tiles:
        stack.add(tile)
        stack.update(get_neighbors(tile))

    while len(stack) > 0:
        tile = stack.pop()
        if tile in seen:
            continue
        seen.add(tile)
        ncount = count_black_neighbors(tile, tiles)
        if tile in tiles and (ncount == 0 or ncount > 2):
            new_tiles.remove(tile)

        elif tile not in tiles and (ncount == 2):
            new_tiles.add(tile)

    return new_tiles
def turn_tiles(tile_steps):
    black_tiles = get_black_tiles(tile_steps)

    for _ in range(100):
        black_tiles = run_day(black_tiles)

    return black_tiles

def solve(filename):
    lines = get_input(filename)
    tile_steps = []
    for line in lines:
        steps = parse_line(line)
        tile_steps.append(steps)

    print(f'A: {len(get_black_tiles(tile_steps))}')

    print(f'B: {len(turn_tiles(tile_steps))}')

if __name__ == "__main__":
    solve("input")

