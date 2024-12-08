from collections import defaultdict
from itertools import combinations

def test():
    ex = """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............"""

    run(ex)


grid_size = -1

def run(input: str):

    # ==== PART 2

    global grid_size
    lines = [[[r] for r in s] for s in input.split("\n")] 

    grid_size = len(lines)
    

    antenna_positions = defaultdict(list)
    for r, row in enumerate(lines):
        for c, col in enumerate(row):
            if "." not in col:
                antenna_positions[col[0]].append((r,c))

    for (freq, pos) in antenna_positions.items():
        antenna_positions[freq] = list(combinations(pos, 2))
                
    check_antennas(lines, antenna_positions)
    pretty_print(lines)

    # ==== PART 2

    lines = [[[r] for r in s] for s in input.split("\n")] 
    for r, row in enumerate(lines):
        for c, col in enumerate(row):
            if "." not in col:
                lines[r][c].append("#")

    check_antennas(lines, antenna_positions, True)
    pretty_print(lines, "2: ")



def check_antennas(lines, antenna_positions, loop=False):

    for freq in antenna_positions:
        for ([r1, c1], [r2, c2]) in antenna_positions[freq]:
            dr, dc = distance((r1,c1), (r2,c2))
            loops = 1
            while loops < 2 if not loop else True: 
                outside = 2
                np1 = (r1 - (dr * loops), c1 - (dc * loops))
                np2 = (r2 + (dr * loops), c2 + (dc * loops))
                if not is_outside(np1):
                    lines[np1[0]][np1[1]].append("#")
                    outside -= 1
                if not is_outside(np2):
                    lines[np2[0]][np2[1]].append("#")
                    outside -= 1
                if outside == 2:
                    break
                loops += 1


def find_antinodes(p1, p2):
    pr_diff = p2[0]-p1[0]
    pc_diff = p1[1]- p2[1]

    p3 = (p1[0] - pr_diff, p1[1] - pc_diff)
    p4 = (p2[0] + pr_diff, p2[1] + pc_diff)
    return p3, p4
        


def distance(r,c):
    dr = (c[0] -  r[0])
    dc = (c[1] - r[1])
    return dr, dc

def is_outside(pos):
    r,c = pos
    return (r < 0 or r >= grid_size) or (c < 0 or c >= grid_size)


def pretty_print(lines, mes="1: ", plot=False):
    pounds = 0
    for line in lines:
        row = "".join([l[-1] for l in line ])
        pounds += row.count("#")
        if plot:
            print(row)
        


    print(mes, pounds)
