from math import prod

def calculate_lines(lines):

    results = []
    for problem in lines:
        op = problem[-1]
        if op == "*":
            result = prod(problem[:-1])
        else:
            result = sum(problem[:-1])

        results.append(result)
    return results


def solve(raw):
    lines = []
    for line in raw:
        try:
            lines.append(list(int(l) for l in line.split()))
        except:
            lines.append(line.split())
    length = len(lines[0])
    compiled = []
    for idx in range(length):
        new_line = []
        for line in lines:
            new_line.append(line[idx])
        compiled.append(new_line)
    results = calculate_lines(compiled)
    print("p1:", sum(results))

def solve_p2(lines):

    lines = [line[::-1] for line in lines]
    built_numbers = []
    new_line = []
    number = ""
    for idx in range(len(lines[0])):
        for line in lines:
            number += line[idx]
        if not number.isspace():
            if number.endswith("+") or number.endswith("*"):
                new_line.append(number[:-1])    
                new_line = list(int(l) for l in new_line)
                new_line.append(number[-1])    
            else:
                new_line.append(number)    
        else:
            built_numbers.append(new_line)
            new_line = []
        number = ""
    built_numbers.append(new_line)
    problems = calculate_lines(built_numbers)
    print("p2:", sum(problems)) 

def parse(input):
    raw = input.split("\n")
    return raw

def run(input):
    parsed = parse(input)
    solve(parsed)
    solve_p2(parsed)
    

def test():
    input="""123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  """

    run(input)
