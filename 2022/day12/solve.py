import os
import string

letters = dict([(char, ord(char) - 96) for char in string.ascii_lowercase])


def inp(name):
    f = f"../inputs/{os.path.split(os.getcwd())[1]}_{name}"
    return {(x, y): c for y, line in enumerate(open(f).readlines())
            for x, c in enumerate(line.strip())}


# MAP = inp("example")
MAP = inp("input")


def is_possible_move(xy, nxy):
    return ord(MAP[nxy].replace("E", "z")) - ord(MAP[xy].replace("S", "a")) <= 1 if nxy in MAP else False


def possible_neighbors(xy):
    return (nxy for nxy in neighbors(xy) if is_possible_move(xy, nxy))


def neighbors(xy):
    (x, y) = xy
    return [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]


def flood(dist, layers):
    edge = set(nxy for xy in layers[-1] for nxy in possible_neighbors(xy) if nxy not in dist)
    dist.update({xy: len(layers) for xy in edge})
    if edge:
        flood(dist, layers + [edge])


def check_distance(start, end):
    dist = {start: 0}
    flood(dist, [{start}])
    return dist[end] if end in dist else 9999


def find_all(values):
    found = [xy for (xy, v) in MAP.items() if v in values]
    return found


def find(val):
    return find_all(val)[0]


print("p1", check_distance(find("S"), find("E")))
print("p2", min(check_distance(start, find("E")) for start in find_all(["S", "a"])))
