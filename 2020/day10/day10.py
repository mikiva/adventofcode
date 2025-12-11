from collections import defaultdict
from datetime import datetime
input_file = "input.txt"

adapters = sorted([int(x) for x in open(input_file)])

adapters_padded = [0] + adapters + [max(adapters) +3]

def a():
    threes, ones = 1, 1

    for j in range(len(adapters) - 1):
        c, n = adapters[j], adapters[j+1]
        if n-c == 1:
            ones += 1
        elif n-c == 3:
            threes += 1

    return threes, ones

  

d = defaultdict(list)
def setup_adapters():
    for i in range(len(adapters_padded)-1):
        n = i + 1
        while adapters_padded[n] - adapters_padded[i] < 4:
            d[adapters_padded[i]].append(adapters_padded[n])
            n += 1
            if n >= len(adapters_padded):
                break

memo ={}
def find_path(l):
    if l[0] == adapters_padded[-1]:
        return 1

    total = 0
    for n in l:
        if n in memo:
            total += memo[n]
        else:
            total += find_path(d[n])
        if n not in memo:
            memo[n] = total
    return total

def b():
    setup_adapters()
    return find_path(d[0])


def run():
    th, on = a()
    print(f'A: {th*on}')
    print(f'B: {b()}')


start_time = datetime.now()
run()
end_time = datetime.now()
tot_time = (end_time - start_time).microseconds / 1000

print(f'Time: {tot_time} ms')
