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
    lines = input.split("\n")
    lines = list(l.split("   ") for l in lines)
    left = sorted(list(int(item[0]) for item in lines))
    right = sorted(list(int(item[1]) for item in lines))
    sorted_lines = list(zip(left,right))
    part1(sorted_lines)
    part2(sorted_lines)


def part1(sorted_lines: list):
    distance = sum((abs(line[0] - line[1])) for line in sorted_lines)
    print(f'1: {distance}')

def part2(lines: list):
    left, right = Counter(int(item[0]) for item in lines), Counter(int(item[1]) for item in lines)
    left, right = Counter(left), Counter(right)
    occurences = 0
    for l, lc in left.items():
        occurences += l * lc * right[l]

    print(f"2: {occurences}")