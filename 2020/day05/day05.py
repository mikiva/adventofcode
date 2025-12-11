from itertools import groupby
from collections import namedtuple

Seat = namedtuple('Seat', ['row', 'col', 'id'])
passes = []

with open("input.txt", "r") as inp:
    passes = inp.read().split("\n")

def seat_id(row, col):
    return row * 8 + col

def get_lower(low, high):
    h =  high - round((high-low) /2.0)
    return int(h)

def get_higher(low, high):
    l = low + round((high-low) / 2.0)
    return int(l)

rows = []
cols = []
seats = []


for ps in passes:
    row = ps[:-3]
    col = ps[-3:]
    l,h,dir_r = 0,127,""
    for r in row:
        dir_r = r
        if r == "F":
            h = get_lower(l,h)
        if r == "B":
            l = get_higher(l,h)
    found_row = l if dir_r == "F" else h

    l,h,dir_c = 0,7, ""
    for c in col:
        dir_c = c
        if c == "L":
            h = get_lower(l,h)
        if c == "R":
            l = get_higher(l,h)

    found_col =   l if dir_c == "L" else h
    s = Seat(int(found_row), int(found_col),seat_id(int(found_row),int(found_col )))
    seats.append(s)

id_sorted_seats = sorted(seats, key=lambda i: i.id, reverse=True)

row_seats = sorted(seats, key=lambda i: i.row)

def find_my_row():
    grouped = groupby(row_seats, key=lambda i: i.row)
    for key, group in grouped:
        on_row = sorted([int(grouped[1]) for grouped in group])
        if key > row_seats[0].row and key < row_seats[-1].row:
            if len(on_row)  == 7:
                return key, on_row
                break

def find_my_col(cols):
    return [x for x in range(cols[0], cols[-1]+1) if x not in cols][0]

my_row, occupied = find_my_row()
my_col = find_my_col(occupied)
my_id = seat_id(my_row, my_col)

print("a", id_sorted_seats[0].id)
print("b", my_id)

