from collections import Counter, defaultdict
import math
from typing import NamedTuple, List

class Borders(NamedTuple):
    top: str = None
    right: str= None
    bottom: str = None
    left: str =None

    def all(self) -> List[str]:
        return [self.top, self.right, self.bottom,self.left]


class Tile:
    def __init__(self,id, lines):
        self.id = id
        self.lines = lines
        self.borders = self.get_borders(self.lines)
    
    def get_borders(self, tile):
        top = tile[0]
        right = "".join([x[-1] for x in tile])
        bottom = tile[-1]
        left = "".join([x[0] for x in tile])

        return Borders(top, right, bottom, left)

def flip_edge(edge):
    e = "".join(edge)
    return min(e, e[::-1])

def read_input(filename):
    tiles = defaultdict(str)
    with open(filename) as inp:
        for t in inp.read().split("\n\n"):
            id = t.split("\n")[0][-5:-1]
            tile = [x for x in t.split("\n")[1:]]
            tiles[id] = tile
    return tiles


#Assume all borders only appear once
def get_corner_tiles(tt):
    corners = []
    edges = Counter()
    product = 1
    for s in range(2):
        for t in tt:

            edge = Borders(
                flip_edge(tt[t][0]),
                flip_edge([x[-1] for x in tt[t]]),
                flip_edge(tt[t][-1]),
                flip_edge([x[0] for x in tt[t]]),
            )
            if s == 0:
                for e in edge:
                    edges[e] += 1
            else:
                if sum(1 for ed in edge if edges[ed] == 1) == 2:
                    product *= int(t)
                    corners.append(Tile(t, tt[t]))
    return corners







def corners_product(corners):
    s = 1
    for x in corners:
        s *= int(x.id)
    return s

def find_neighbor(tiles, borders, id):
    #print(borders)
    neighbors = defaultdict(str)
    for b in borders[id]:

        for flipped in range(2):
            border = b[::-1] if flipped else b
           # print(border)
            for t in tiles:
                if border in borders[t] and t != id:
                    neighbors[t] = (t, border, flipped)
    #print(neighbors)
    return neighbors

def solve_2(tiles, corners):
    width = int(math.sqrt(len(tiles)))
    #print(width)
    assembled_tiles = defaultdict(str)
    corner_tiles = get_corner_tiles(tiles)
    grid = [-1] * width
    for i in range(width):
        grid[i] = [-1] * width
        #print(grid[i])

def solve(filename):
    tiles = read_input(filename)
    corner_tiles = get_corner_tiles(tiles)
    print(f'A: {corners_product(corner_tiles)}')

    #print(f'B: {solve_2(tiles, corner_tiles)}')


if __name__ == "__main__":
    solve("ex")