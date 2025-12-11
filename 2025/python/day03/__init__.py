def find_joltage(line):
    new_line = list(line)
    max_1 = new_line.index(max(new_line))
    
    if max_1 == len(line) - 1:
        new_line.pop()
    else:
        new_line[max_1] = -1
    indicies = []
    while True:
        max_2 = new_line.index(max(new_line))
        if max_2 < max_1 and len(line) == len(new_line):
            new_line[max_2] = -1
        else:
            indicies = sorted([max_1, max_2])
            break
    value = int(str(line[indicies[0]]) + str(line[indicies[1]]))
    return value



def find_joltage_p2(bank, current, remainder=12):
    line = list(bank)
    if remainder == 0:
        battery = "".join(str(l) for l in current)
        return int(battery)
    if remainder == 1:
        to_check = line[:]
    else:
        to_check = line[:-remainder+1]
    max_1 = to_check.index(max(to_check))
    current.append(line[max_1])
    new_line = line[max_1+1:]
    return find_joltage_p2(new_line, current, remainder-1)

def parse(input):
    lines = input.split("\n")
    parsed = []
    for line in lines:
        parsed.append(list(int(l) for l in line))
    return parsed
    
        


def solve(input, part=1):

    batteries = []
    for line in input:
        if part == 1:
            batt = find_joltage(line)
        else:
            batt = find_joltage_p2(line, [])
        batteries.append(batt)

    print("p1:" if part == 1 else "p2:" , sum(batteries))


def run(input):
    solve(parse(input))
    solve(parse(input), 2)

def test():
    input = """987654321111111
811111111111119
234234234234278
818181911112111"""

    solve(parse(input))
    solve(parse(input), 2)
