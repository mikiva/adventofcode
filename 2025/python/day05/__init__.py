import sys


def solve(fresh, ingredients):
    are_fresh = 0
    for ing in ingredients:
        for st, en in fresh:
            if ing >= st and ing <= en:
                are_fresh += 1
                break
    print("p1:", are_fresh)

def update_ranges(current, new_range):
    new_start, new_end = new_range
    updated_start, updated_end = -sys.maxsize, sys.maxsize
    is_outside_existing = True
    for idx, [c_start, c_end] in enumerate(current):
        if not (new_end < c_start or new_start > c_end):
            is_outside_existing = False
            
            if new_start < c_start:
                updated_start = new_start
            else:
                updated_start = c_start
            if new_end > c_end:
                updated_end = new_end
            else:
                updated_end = c_end

            current[idx][0] = updated_start
            current[idx][1] = updated_end
            break

    if is_outside_existing:
        current.append([new_start, new_end])


    return current
def get_all_ids(fresh):

    all_ids = []
    for s, e in fresh:
        all_ids.append([s,e])
    new_ranges = []
    updated_ranges = []

    for s,e in all_ids:
        updated_ranges = update_ranges(new_ranges, [s,e])
        new_ranges = updated_ranges[:]
    
    # For some reason all of this need a second lap. Not sure why.
    new_ranges = []
    new_updated = []
    for s,e in updated_ranges:
        new_updated = update_ranges(new_ranges, [s,e])

        new_ranges = new_updated[:]

    diffs = 0

    for sta, end in new_updated:
        diffs += (end-sta)+1

    print("p2:", diffs)

def parse(input):
    fresh, ingredients = input.split("\n\n")
    all_ranges = set()
    for fr in fresh.split("\n"):
        s,e = fr.split("-")
        all_ranges.add((int(s), int(e)))


    
    ingredients = set(int(i) for i in ingredients.split("\n"))
    return all_ranges, ingredients
def run(input):
    fresh, ingredients = parse(input)
    solve(fresh, ingredients)

    get_all_ids(fresh)

def test():
    input="""3-5
10-14
16-20
12-18

1
5
8
11
17
32"""
    run(input)