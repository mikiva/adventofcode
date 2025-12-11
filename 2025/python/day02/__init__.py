import re

re_pattern = r"(\w+)\1+"


def find_matches_p1(p):
    if len(p)%2 != 0:
        return False
    st = p[:len(p)//2]
    en = p[len(p)//2:]
    return st == en

def find_matches_p2(p_id):
    groups = re.findall(re_pattern, str(p_id))
    for match in groups:
        return (match*150).startswith(p_id*3) and not (match.startswith("0"))

def solve(input, part=1):
    all_matches = []
    for interval in input:
        interval_matches = []
        for pid in range(interval[0], interval[1] +1):
            p = str(pid)
            if part == 1:
                if find_matches_p1(p):
                    interval_matches.append(pid)
            else:
                if find_matches_p2(p):
                    interval_matches.append(pid)
        all_matches.append(interval_matches)

    count_them = 0

    for matches in all_matches:
        count_them += sum(matches)
        
    print("p1:" if part == 1 else "p2:", count_them)


def parse(input):
    intervals = input.split(",")
    ranges = [(int(s),int(f)) for s,f in[x.split("-") for x in intervals]]
    return ranges

def run(input):
    ranges = parse(input)

    solve(ranges)
    solve(ranges, 2)

def test():
    input = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"
    run(input)

