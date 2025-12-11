from collections import namedtuple
codes = list()
Code = namedtuple('Code', ['visited', 'op', 'val'])

with open("input.txt", "r") as inp:
    for line in [x.split() for x in inp.readlines()]:
        codes.append(Code(False, line[0], int(line[1])))

def a(instructions):
    data = instructions.copy()
    acc, loc = 0, 0
    exits = False
    while True:
        if loc >= len(data):
            exits = True
            break
        code = data[loc]
        
        if code.visited:
            break

        data[loc] = code._replace(visited = True)
        op, val = code.op, code.val
        if op == "nop":
            loc += 1
        elif op == "jmp":
            loc += val
        elif op == "acc":
            acc += val
            loc += 1
    return exits, acc

def change(op):
    return 'jmp' if op == 'nop' else 'nop'

def b():
    for i in range(len(codes)):
        data = codes.copy()
        op = data[i].op
        if op in ['jmp', 'nop']: 
            data[i] = data[i]._replace(op = change(op))
        else:
            continue
        exits, acc = a(data)
        if exits: 
            return acc


print("a", a(codes)[1])
print("b", b())
