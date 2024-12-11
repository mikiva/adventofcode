
from collections import defaultdict
def test():
    #ex = """0 1 10 99 999"""
    ex = """125 17"""

    run(ex)

def run(input: str):
    stones = [s for s in input.split(" ")]

    stones_one = blink_twenty_five(stones)
    stones_two = blink_seventy_five(stones)

    print("1: ", len(stones_one))
    #print("2: ", stones_two)



def blink_seventy_five(sts):

    counter = defaultdict(int)
    stones = sts[:]
    
    for stone in stones:
        counter[stone] += 1

    for count in range(75):
        #print(list(counter.keys()))
        #print(stones)
        stones = blink_once(list(counter.keys()))
        #print(stones)
        
        for stone in stones:
            counter[stone] += 1
        if count == 25:
            break


    stone_count = sum(list(counter.values()))
    return stone_count
    ...


def blink_twenty_five(sts):
    stones = sts[:]
    for _ in range(25):
        stones = blink_once(stones)        

    return stones

def blink_once(stones):
    blinked = []
    for stone in stones:
        if stone == "0":
            blinked.append("1")

        elif len(stone) % 2 == 0:
            left = int(stone[0:len(stone)//2])
            right = int(stone[len(stone)//2:])
            blinked.extend([str(left), str(right)])

        else:
            new_stone = int(stone) * 2024
            blinked.append(str(new_stone))
    return blinked

#259884 too low
#259892 too low
#265978 too low