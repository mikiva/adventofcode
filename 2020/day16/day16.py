from ast import parse
from os import posix_fadvise
import re
from collections import defaultdict
data = ""


### PART 1 ###

def parse_valid_fields(data):   
    valid = set()
    valid_part = data.split("\n\n")[0]
    matcher = re.compile("([0-9]+-[0-9]+)")
    vals = re.findall(matcher, valid_part)
    for val in vals:
        low, high = val.split("-")
        for v in range(int(low), int(high)+1):
            valid.add(v)

    return valid



def parse_nearby_tickets(data):
    valid_part = data.split("\n\n")[2]
    ticket_numbers = valid_part.split("\n")[1:]
    numbers = []
    tickets = []
    for ticket in ticket_numbers:
        tick = []
        for number in [int(x) for x in ticket.split(",")]:
            tick.append(number)
        tickets.append(tick)


    return tickets

def find_invalid_numbers(valid, tickets):
    invalid =[]
    for tick in tickets:
        invalid.extend([x for x in tick if x not in valid])

    return invalid

def solve_part_1():
    valid = parse_valid_fields(data)
    nearby_tickets = parse_nearby_tickets(data)
    invalid = find_invalid_numbers(valid, nearby_tickets)
    return sum(invalid)


### PART 2 ###

def solve_part_2():
    my_ticket = parse_my_ticket(data)
    notes = parse_notes(data)

    intervals = set()
    for n in notes:
        for i in notes[n]:
            intervals.add(i)

    nearby_tickets = parse_nearby_tickets(data)
    valid_tickets = parse_valid_tickets(nearby_tickets, intervals)
    valid_tickets.append(my_ticket)
    possible_fields = []
    for fieldIndex in range(len(valid_tickets[0])):

        working_fields = []
        for note in notes:
            works = True
            for ticket in valid_tickets:
                if ticket[fieldIndex] not in notes[note]:
                    works = False
                    break
            if works:
                working_fields.append(note)
        
        possible_fields.append(working_fields)

    true_range = [-1] * 20


    for i in range(len(true_range)):
        for pos in range(len(valid_tickets[0])):
            if len(possible_fields[pos]) == 1 and true_range[pos] == -1:
                break

        taken_field = possible_fields[pos][0]
        true_range[pos] = taken_field
        for other in range(len(possible_fields)):
            if other == pos:
                continue
            if taken_field in possible_fields[other]:
                possible_fields[other].remove(taken_field)


    important_seats = []
    for idx, field in enumerate(true_range):
        if field.startswith("departure"):
            important_seats.append([idx, field])
    total = 1
    for imp in important_seats:
        total = total * my_ticket[imp[0]]
    
    return total


##Filter invalid tickets. Look in ticket, compare with intervals
def parse_valid_tickets(numbers, interval):
    valid_tickets = []
    for ticket in numbers:
        valid = True
        for x in ticket:
            if x not in interval:
                valid = False
        if valid:                
            valid_tickets.append(ticket)



    return valid_tickets
        


def get_intervals(data):
    intervals = []
    for d in data:
        low, high = d.split("-")
        for val in range(int(low), int(high)+1):
            intervals.append(val)
    return intervals

def parse_notes(data):
    notes = defaultdict(list)

    raw_notes = data.split("\n\n")[0]

    capture_notes_pattern = "(^[a-z\s]+): ([0-9]+-[0-9]+) or ([0-9]+-[0-9]+)"
    matcher = re.compile(capture_notes_pattern)

    for n in raw_notes.split("\n"):
        matched = re.findall(matcher, n)[0]
        notes[matched[0]] = get_intervals(matched[1:])

    return notes

def parse_my_ticket(data):
    my_ticket =[int(x) for x in data.split("\n\n")[1].split("\n")[1:][0].split(",")]

    return my_ticket


def get_position(tickets, notes, pos):
    numbers = [x[pos] for x in tickets]
    ticket = {}
    for note in notes:
        count = 0
        for num in numbers:
            #print(num, notes[note])
            if num not in notes[note]:
                print(num, notes[note])
                return None
        
        return note



def solve():
    print(f'A: {solve_part_1()}')
    print(f'B: {solve_part_2()}')



if __name__ == "__main__":
    with open("input") as inp:
        data = inp.read()
    solve()