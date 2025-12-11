validA = 0
validB = 0
    

def format_line(line):
    parts = line.split(" ")
    password = parts[-1]
    letter = parts[-2][0]
    interval = dict(min=int(parts[0].split("-")[0]), max=int(parts[0].split("-")[1]))
    return interval, letter, password

def check_A(line):
    global validA
    pw = format_line(line)
    nbr = len([l for l in pw[2] if l == pw[1]])
    if nbr <= pw[0]['max'] and nbr >= pw[0]['min']:
        validA = validA + 1

def check_B(line):
    global validB
    formatted = format_line(line)
    try:
        i = formatted[0]   
        l = formatted[1]
        p = formatted[2]

        if p[i['min']-1] == l and p[i['max']-1] == l:
            pass
        elif p[i['min']-1] == l or p[i['max']-1] == l:
            validB = validB + 1
    except:
        pass

with open("input.txt") as inp:
    for line in inp:
        check_A(line)
        check_B(line)
    

print(f'1: {validA}')
print(f'2: {validB}')



