from collections import Counter



def test():
    ex_input = """3   4
4   3
2   5
1   3
3   9
3   3"""


    run(ex_input)

def run(input: str):
    part1(input)
    part2(input)


def part1(input: str):
    lines = input.strip().split("\n")
    lines = list(l.split("   ") for l in lines)
    left = sorted(list(int(item[0]) for item in lines))
    right = sorted(list(int(item[1]) for item in lines))
    sorted_lines = list(zip(left,right))
    distance = sum((abs(line[0] - line[1])) for line in sorted_lines)
    print(f'1: {distance}')

def part2(input: str):
    lines = input.strip().split("\n")
    lines = list(l.split("   ") for l in lines)
    left, right = Counter(int(item[0]) for item in lines), Counter(int(item[1]) for item in lines)
    left, right = Counter(left), Counter(right)
    occurences = 0
    for l, lc in left.items():
        occurences += l * lc * right[l]

    print(f"2: {occurences}")