import os
from collections import defaultdict
from time import time

f = f"../inputs/{os.path.split(os.getcwd())[1]}_ex2.txt"
instructions = [line.split() for line in open(f).read().split("\n")]
instructions = [(direction, int(dist)) for direction, dist in instructions]

dirs = {
    "R": (0, 1),
    "L": (0, -1),
    "U": (-1, 0),
    "D": (1, 0)
}


def p1():
    visited = set()

    pos, pos_t = (0, 0), (0, 0)
    visited.add(pos_t)
    for direction, dist in instructions:
        dx, dy = dirs[direction]
        for _ in range(dist):
            x, y = pos
            new_pos = (x + dx, y + dy)
            hx, hy = new_pos
            tx, ty = pos_t

            if abs(hx - tx) > 1 or abs(hy - ty) > 1:
                new_pos_t = (x, y)
                pos_t = new_pos_t
                visited.add(new_pos_t)
            pos = new_pos
    return len(visited)


def p2():
    visited = set()
    tail_length = 9
    tail = [(0, 0) for _ in range(tail_length)]
    pos = (0, 0)
    pos_t = (0, 0)
    for direction, dist in instructions:
        dx, dy = dirs[direction]
        for _ in range(dist):
            x, y = pos
            new_pos = (x + dx, y + dy)
            cur_tail = pos
            for i, (tx, ty) in enumerate(tail):
                if i == 0:
                    hx, hy = new_pos
                else:
                    hx, hy = cur_tail

                if abs(hx - tx) > 1 or abs(hy - ty) > 1:
                    new_pos_t = (x, y)
                    tail[i] = new_pos_t

                    if i == 8:
                        visited.add(new_pos_t)

                cur_tail = (tx, ty)

            pos = new_pos

    return len(visited)


print("p1", p1(), p1() in [13, 5735])
print("p2", p2())
