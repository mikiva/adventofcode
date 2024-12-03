import re
def test():
    #ex1 = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
    ex2 = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

    run(ex2)

def run(input):
    p1 = part1(input)
    p2 = part2(input)
    print(f"1: {p1}")
    print(f"2: {p2}")
    

def part1(input: str):
    muls = re.findall("(mul\(\d+,\d+\))", input)
    total = 0
    for mul in muls:
        total += evaluateMul(mul)

    return total

def evaluateMul(mul: str):
    [a,b] = re.findall("(\d+)", mul)
    return int(a)*int(b)


def part2(input: str):
    alls = re.findall("(do\(\))|(don\'t\(\))|(mul\(\d+,\d+\))", input)
    enabled = True
    total = 0
    for instruction in alls:
        do, dont, mul = instruction

        if do:
            enabled = True
        elif dont:
            enabled = False
        elif mul and enabled:
            total += evaluateMul(mul)
    return total

