

def run(input):

    zero_counts = 0
    pass_zero_counts = 0
    pos = 50
    for data in input.split("\n"):
        direction, value = data[0], int(data[1:])
        
        for _ in range(value):
            pos = (pos - 1 if direction == "L" else pos +1 ) % 100
            if pos == 0:
                pass_zero_counts += 1
        if pos == 0:
            zero_counts +=1 

    print(zero_counts)
    print(pass_zero_counts)



