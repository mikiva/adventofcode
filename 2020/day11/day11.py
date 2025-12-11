import collections
from copy import deepcopy

import time

start = time.time()

orig = [list(x.strip("\n")) for x in  open("input.txt")]


grid = deepcopy(orig)
rows = len(orig)
cols = len(orig[0])

# A
def check_neigh(r, c, temp):
    if temp[r][c] == "L":
        for cr in [-1,0,1]:
            for cc in [1,0,-1] :
                if r+cr < 0 or c+cc < 0: continue
                try:
                    if cr == 0 and cc == 0: 
                        continue
                    elif temp[r+cr][c+cc] == "#":
                        return "L"
                except:
                    continue
        return "#"
    elif temp[r][c] == "#":
        count = 0
        for cr in [1, 0, -1]:
            for cc in [1,0,-1] :
                if r+cr < 0 or c+cc < 0: continue
                try:
                    if cr == 0 and cc == 0: 
                        continue
                    elif temp[r+cr][c+cc] == "#": 
                        count = count+1
                except:
                    continue
        if count > 3: 
            return "L"
        else: return "#"
    elif temp[r][c] == ".": return "."



def get_new_seats(current):
    
    grid = deepcopy(current)
    for r, row in enumerate(current):
        for c, col in enumerate(row):
            grid[r][c] = check_neigh(r,c, current)
    return grid



def check_neigh_long(r,c,seats):

    seat = seats[r][c]
    if seat == "L":
        # Up
        rr = r - 1
        rc = c
        found_occupied = False
        while rr >= 0:
            if seats[rr][rc] != ".":
                if seats[rr][rc] == "#":
                    found_occupied = True
                break
            rr -= 1
        # Down
        rr = r + 1
        rc = c
        while rr < rows:
            if seats[rr][rc] != ".":
                if seats[rr][rc] == "#":
                    found_occupied = True
                break
                
            rr += 1
        # Left
        rr = r
        rc = c - 1
        while rc >= 0:
            if seats[rr][rc] != ".":
                if seats[rr][rc] == "#":
                    found_occupied = True
                break
                
            rc -= 1
        # Right
        rr = r
        rc = c + 1
        while rc < cols:
            if seats[rr][rc] != ".":
                if seats[rr][rc] == "#":
                    found_occupied = True
                break
                
            rc  += 1 
        # Up-right
        rr = r - 1
        rc = c + 1
        while rc < cols and rr >= 0:
            if seats[rr][rc] != ".":
                if seats[rr][rc] == "#":
                    found_occupied = True
                break
                
            rr -= 1
            rc += 1
        # Down-right
        rr = r + 1
        rc = c + 1
        while rc < cols and rr < rows:
            if seats[rr][rc] != ".":
                if seats[rr][rc] == "#":
                    found_occupied = True
                break
                
            rr += 1
            rc += 1
        # Down-left
        rr = r + 1
        rc = c - 1
        while rc >= 0 and rr < rows:
            if seats[rr][rc] != ".":
                if seats[rr][rc] == "#":
                    found_occupied = True
                break
                
            rr += 1
            rc -= 1
        # Up-left
        rr = r - 1
        rc = c - 1
        while rc >= 0 and rr >= 0:
            if seats[rr][rc] != ".":
                if seats[rr][rc] == "#":
                    found_occupied = True
                break
                
            rr -= 1
            rc -= 1
        return "#" if not found_occupied else "L"
    elif seat == "#":
        count = 0
        # Up
        rr = r - 1
        rc = c
        while rr >= 0:
            if seats[rr][rc] != ".":
                if seats[rr][rc] == "#":
                    count += 1
                break
            rr -= 1
        # Down
        rr = r + 1
        rc = c
        while rr < rows:
            if seats[rr][rc] != ".":
                if seats[rr][rc] == "#":
                    count += 1
                break
            rr += 1
        # Left
        rr = r
        rc = c - 1
        while rc >= 0:
            if seats[rr][rc] != ".":
                if seats[rr][rc] == "#":
                    count += 1
                break
            rc -= 1
        # Right
        rr = r
        rc = c + 1
        while rc < cols:
            if seats[rr][rc] != ".":
                if seats[rr][rc] == "#":
                    count += 1
                break
            rc += 1
        # Up-right
        rr = r - 1
        rc = c + 1
        while rc < cols and rr >= 0:
            if seats[rr][rc] != ".":
                if seats[rr][rc] == "#":
                    count += 1
                break
            rr -= 1
            rc += 1

        # Down-right
        rr = r + 1
        rc = c + 1
        while rc < cols and rr < rows:
            if seats[rr][rc] != ".":
                if seats[rr][rc] == "#":
                    count += 1
                break
            rr += 1
            rc += 1
        # Down-left
        rr = r + 1
        rc = c - 1
        while rc >= 0 and rr < rows:
            if seats[rr][rc] != ".":
                if seats[rr][rc] == "#":
                    count += 1
                break
            rr += 1
            rc -= 1
        # Up-left
        rr = r - 1
        rc = c - 1
        while rc >= 0 and rr >= 0:
            if seats[rr][rc] != ".":
                if seats[rr][rc] == "#":
                    count += 1
                break
            rr -= 1
            rc -= 1

        if count >= 5: 
            return "L"
        else: 
            return "#"
    elif seat == ".": 
        return "."


    


def get_new_seats_long(current):
    grid = deepcopy(current)
    for r, row in enumerate(current):
        for c, col in enumerate(row):
            grid[r][c] = check_neigh_long(r,c, current)

    return grid


def a():
    
    current = deepcopy(orig)
    while True:
        new_seats = get_new_seats(current)
        if current == new_seats:
            break
        current = new_seats
    return new_seats


def b():

    current = deepcopy(orig)
    
    while True:
        new_seats = get_new_seats_long(current)
        if current == new_seats:
            break
        current = new_seats
    return new_seats



def count_occupied(seats):
    occupied = 0
    for row in seats:
        for col in row:
            if col == "#": occupied += 1
    return occupied

def run():
    print(f'A: {count_occupied(a())}')
    print(f'B: {count_occupied(b())}')

run()


end = time.time()

total = end-start
print("TIME", total)