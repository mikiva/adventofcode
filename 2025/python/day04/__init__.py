def look_around(rows, y, x):
    positions = [(x-1, y), (x-1, y-1), (x, y-1), (x+1, y),
                 (x+1, y+1), (x, y+1), (x+1, y-1), (x-1, y+1)]

    rolls = 0
    for pos in positions:
        if pos[0] < 0 or pos[1] < 0:
            continue
        try:
            if rows[pos[1]][pos[0]] == "@":
                rolls += 1
            if rolls > 3:
                return False
        except:
            continue
    return True


def solve(input, part=1):
    accessable = set()
    for iy, y in enumerate(input):
        for ix, x in enumerate(y):
            if x == "@" and look_around(input, iy, ix):
                accessable.add((iy, ix))
    if part == 1:
        print("p1:", len(accessable))
    if part == 2:
        for acc in accessable:
            input[acc[0]][acc[1]] = "."
    return accessable


def parse(input):
    parsed = []
    rows = input.split("\n")
    for row in rows:
        parsed.append(list(c for c in row))
    return parsed


def run(input):
    parsed = parse(input)
    solve(parsed)

    count = 0
    accessable = set()
    new_input = parsed[:]
    while True:

        new_accessable = solve(new_input, 2)
        if count > 0 and len(new_accessable) == 0:
            break
        accessable.update(new_accessable)
        count += 1
        if count > 1000_000:
            print("too many loops")
            break
    print("p2:", len(accessable))


def test():
    input = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""

    run(input)
