from itertools import combinations

terms = [2, 3]
lines = []

with open("input.txt", "r") as inp:
    for line in inp:
        lines.append(int(line))

def multiply(factors):
    res = 1
    for f in factors:
        res = res * f
    return res


for term in terms:
    for c in combinations(lines, term):
        if sum(c) == 2020:
            print(f'{term}: {multiply(c)}')
            break