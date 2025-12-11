import re
def read_input(file):
    lines = open(file).read().split("\n")
    return lines

def calculate_items(a,b, op):
    if op == "*":
        return a * b
    elif op == "+":
        return a + b


def calculate_line(line, op):
    current, current_op = 0, op
    for idx, item in enumerate(line):
        if item == "+" or item == "*":
            current_op = item
        else:
            current = calculate_items(current, int(item), current_op)

    return current


def calc(line, part):
    if part == 1:
        tot, op = 0, "+"
        for item in line.split():
            if item == "*" or item == "+":
                op = item
            else:
                tot = calculate_items(tot, int(item), op)
    if part == 2:
        tot = 1
        line = line.split("*")
        for i,l in enumerate(line):
            if "+" in l:
                linesum = sum([int(x.strip()) for x in l.split("+") ])
                line[i] = linesum
            
        for k in [int(x) for x in line]:
            if k < 1:
                k = 1
            tot = tot * k
        


    return tot

def get_parenthesis(line, part):
    openp, closep = 0, 0
    ind, out = 0,0
    for i,v in  enumerate(line):
        if v == "(":
            openp += 1
            if openp == 1:
                ind = i+1
        elif v == ")":
            closep += 1
            if openp == closep:
                out = i
                break
            
    if openp == 0:
        return calc(line, part)

    new_line = line[:ind-1] + str(get_parenthesis(line[ind:out], part)) + line[out+1:]
    return get_parenthesis(new_line, part)
            

def start_calculation(lines, part):
    sums = 0
    for line in lines:
        tots = get_parenthesis(line, part)
        sums += tots
    return sums


def solve():
    lines = read_input("input")
    print(f'A: {start_calculation(lines, 1)}' )
    print(f'B: {start_calculation(lines, 2)}')

if __name__ == "__main__":

    solve()
