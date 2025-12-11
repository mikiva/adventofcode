from collections import defaultdict

def read_input():
    #input=".#.\n..#\n###"
    input = open("input").read()
    grid = []
    for row in input.split("\n"):
        r = []
        for cell in row:
            r.append(cell)
        grid.append(r)
    return grid

def get_init_active(grid):
    active = set()

    for i,v in enumerate(grid):
        for ii,vv in enumerate(v):
            if vv == "#":
                active.add((i,ii, 0,0))

    return active


def cycle(dims, active):

    new_active = defaultdict(int)

    for x,y,z,w in active:
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                for dz in [-1, 0, 1]:
                    for dw in [-1, 0, 1] if dims > 3 else [0]:
                        if dx == 0 and dy == 0 and dz == 0 and dw == 0:
                            continue
                        new_active[(x+dx, y+dy, z+dz, w+dw)] += 1
    current_active = {p for p, v in new_active.items() if v == 3 or (v == 2 and p in active) }
    return current_active


def do_cycles(active, dims):
    for i in range(6):
        active = cycle(dims, active)

    return len(active)


def solve(active):
    print(f'A: {do_cycles(active,3)}')
    print(f'B: {do_cycles(active,4)}')
    

if __name__ == "__main__":
    active = get_init_active(read_input())
    solve(active)
