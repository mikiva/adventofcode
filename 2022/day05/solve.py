import os
import re
from collections import defaultdict

f = f"../inputs/{os.path.split(os.getcwd())[1]}.txt"

stacks, instructions = [p for p in open(f).read().split("\n\n")]


# BOXES

def get_stacks():
    crate_stacks = defaultdict(list)
    crates_p = r"(\[[A-Z]\])"
    for stack in stacks.split("\n")[:-1]:
        for n in re.finditer(crates_p, stack):
            val, pos = n.group(), n.start(0)
            crate_stacks[(pos // 4) + 1].insert(0, val[1])
    return crate_stacks


# box_stacks = bs
# INSTRUCTIONS

def p1(box_stacks):
    moves = r"\d+"
    for inst in instructions.split("\n"):
        count, fr, to = [int(i) for i in re.findall(moves, inst)]
        for _ in range(count):
            b = box_stacks[fr].pop()
            box_stacks[to].append(b)

    stack_dicts = sorted(box_stacks.items())

    last_items = "".join([v[-1] for k, v in stack_dicts])
    return last_items


def p2(box_stacks):
    moves = r"\d+"

    for inst in instructions.split("\n"):
        to_move = []
        count, fr, to = [int(i) for i in re.findall(moves, inst)]
        for _ in range(count):
            to_move.append(box_stacks[fr].pop())
        to_move.reverse()
        box_stacks[to].extend(to_move)
    stack_dicts = sorted(box_stacks.items())

    last_items = "".join([v[-1] for k, v in stack_dicts])
    return last_items


print("p1", p1(get_stacks()))
print("p2", p2(get_stacks()))
print("===")
