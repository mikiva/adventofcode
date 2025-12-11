import os
import string

f = f"../inputs/{os.path.split(os.getcwd())[1]}.txt"

lines = [l for l in open(f).read().split("\n")]

prios = {j: k + 1 for k, j in enumerate(string.ascii_letters)}


def p1():
    r = [(set(l[:len(l) // 2]), set(l[len(l) // 2:])) for l in lines]
    return sum([prios[c1.intersection(c2).pop()] for c1, c2 in r])

def p2():
    total = 0
    for i in range(0, len(lines), 3):
        g1 = set(lines[i])
        g2 = set(lines[i + 1])
        g3 = set(lines[i + 2])
        total += prios[set.intersection(g1, g2, g3).pop()]
    return total


print(p1())
print(p2())
assert p1() == 7990
assert p2() == 2602
