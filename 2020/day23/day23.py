from collections import deque
from copy import deepcopy
#inp = 389125467
inp = 974618352
input = deque(int(x) for x in str(inp))

number_of_mugs = 10 ** 6

def fill_mug_circle(mugs, part2=False):
    max_mugs = max(mugs)
    new_mugs = [-1] * (number_of_mugs+1)
    for m in range(len(mugs)-1):
        new_mugs[mugs[m]] = mugs[m+1]
    new_mugs[mugs[-1]] = max(mugs)+1
    for i in range(max(mugs)+1, number_of_mugs):
        new_mugs[i] = i+1
    new_mugs[number_of_mugs] = mugs[0]
    return new_mugs
def rotate_mugs(curr, r, mugs):
    while True:
        if mugs[r] == curr:
            return mugs
        else:
            mugs.rotate(1)
def play(mugs, rounds):
    c = 0
    put_aside = []
    current = mugs[c]
    for r in range(rounds):
        idx = mugs.index(current)
        c = idx
        for _ in range(3):
            put_aside.append(mugs[(idx+1) % len(mugs)])
            mugs.remove(mugs[(idx+1) % len(mugs)])
        target = None
        found = False
        diff = 1
        while not found:
            ch = idx
            for _ in range(len(mugs)):
                ch = (ch+1) % len(mugs)
                next = mugs[ch]
                if current - diff == next:
                    found = True
                    target = next
                    break
                elif current - diff < min(mugs):
                    found = True
                    target = max(mugs)
                    break

            diff += 1
        current = mugs[(idx+1) % len(mugs)]

        nm = mugs
        put_aside.reverse()
        for l in put_aside:
            nm.insert(nm.index(target) + 1 % len(nm), l)
        put_aside.clear()
        mugs = nm
        c = (c+1) % len(mugs)
        mugs = rotate_mugs(current, idx, mugs)
    return mugs

def play2(mugs, current):
    put_aside = []
    put_aside.append(mugs[current])
    for _ in range(2):
        put_aside.append(mugs[put_aside[-1]])

    
    mugs[current] = mugs[put_aside[-1]]

    target = current - 1

    while target in put_aside or target == 0:
        target -= 1
        if target < 1:
            target = number_of_mugs

        
    mugs[put_aside[-1]] = mugs[target]
    mugs[target] = put_aside[0]

    return mugs, mugs[current]

def part_1():
    rounds = 100
    p = play(deepcopy(input), rounds)
    idx = p.index(1)
    ans = []
    for _ in range(len(p)):
        ans.append(p[idx % len(p)])
        idx += 1
    mugs = rotate_mugs(1, 0, p)
    mugs.remove(1)
    mugs_str = "".join(map(str, mugs))
    return mugs_str

def part_2():
    mugs = fill_mug_circle(list(input))
    rounds = 10 ** 7
    current = input[0]
    for _ in range(rounds):
        mugs, current = play2(mugs, current)
    first_mug = mugs[1]
    second_mug = mugs[first_mug]
    return first_mug * second_mug
def solve():
    print(f'A: {part_1()}')
    print(f'B: {part_2()}')

if __name__ == "__main__":
    solve()
