
def test():
    ex = '''7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9'''.strip()

    run(ex)

def run(input: str):
    lines = list(report.split() for report in input.strip().split("\n"))
    reports = []
    for line in lines:
        reports.append(list(int(l) for l in line))
                
    safe, _ = part1(reports)
    safe_p2 = part2(reports)
    print(f"1: {len(safe)}")
    print(f"2: {len(safe_p2)}")


def part1(reports: list):
    safe_reports = []
    unsafe = []
    for line in reports:
        if check_line_p1(line):
            safe_reports.append(line)
        else:
            unsafe.append(line)
    return safe_reports, unsafe       


def check_line_p1(line: list):
    if not (sorted(line) == line) and not (sorted(line, reverse=True) == line):
        return False
    for idx in range(len(line) -1):
        a,b = line[idx], line[idx+1]
        if not (abs(a-b) in [1,2,3]):
            return False
    return True


def part2(reports: list):
    safe_reports, check_again = part1(reports)
    for again in check_again:
        for ignore in range(len(again)):
            if check_line_p2(again, ignore):
                safe_reports.append(again)
                break
    return safe_reports

def check_line_p2(line: list, ignore):
    new_line = line.copy()
    new_line.pop(ignore)
    return check_line_p1(new_line)