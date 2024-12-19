from collections import defaultdict
import re
def test():
    ex = """r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb"""

    run(ex)


def run(input: str):
    towels, desired = input.split("\n\n")
    towels = towels.split(", ")
    desired = desired.split("\n")
    possible_designs = []
    memo = dict()
    for design in desired:
        possible_parts = []
        for towel in towels:
            if towel in design:
                possible_parts.append(towel)
        if len(possible_parts) > 0:
            if try_design(memo, design, possible_parts):
                possible_designs.append(design)

    print("1: ", len(possible_designs))
def try_design(memo: dict, design: str, parts):
    if design == "":
        return True
    if design in memo:
        return memo[design]
    for part in parts:
        if design.startswith(part):
            if try_design(memo, design[len(part):], parts):
                memo[design] = True
                return True
    memo[design] = False
    return memo[design]
