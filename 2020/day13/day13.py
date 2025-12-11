

with open("input.txt") as inp:
    time = int(inp.readline())
    ids = [int(x) if x.isdigit() else x for x in inp.readline().split(",")]

def a():
    close, i = time, 0
    for id in [int(x) for x in ids if x != "x"]:
        if id - (time % id) < close:
            close, i = (id - (time % id)), id
        
    return i * close


def b():
    bids = [b for b in ids if b != "x"]
    remainders = [-i%v for i,v in enumerate(ids) if v != 'x']
    tstamp, step = 0, 1
    for bid, rem in zip(bids, remainders):
        while tstamp % bid != rem:
            tstamp += step
        step *= bid
    return tstamp

def run():
    print (f'A: {a()}')
    print (f'B: {b()}')

run()