import re
def test():
    ex = """1
10
100
2024"""
    ex2 = "123"

    ex3 = """1
2
3
2024"""



    run(ex3)


def run(input: str):
    numbers = list(int(i) for i in input.split("\n"))
    

    new_secrets = []
    changes = []
    track_numbers = []
    for buyer, number in enumerate(numbers):
        next_number = number

        changes.append([None])
        track_numbers.append(next_number % 10)
            
        for idx in range(1, 2001):

            next_number = get_next_number(next_number)
            track_numbers.append(next_number % 10)
            changes[buyer].append((track_numbers[idx]) - (track_numbers[idx-1]) )
            
        new_secrets.append(next_number)

    #pattern = "-2,1,-1,3"
    #for buyer in changes:
    #    buy_string = ",".join(str(i) for i in buyer)
    #    try:
    #        found = buy_string.index(pattern)
    #        print(found)
    #    except:
    #        print("found_none")
    #        continue
    #    
    #    #print(buy_string)




    print("1: ", sum(new_secrets))

def get_next_number(secret: int) -> int: 

    next_num = secret*64
    next_num = mix(next_num, secret)
    next_num = prune(next_num)

    next_secret = next_num // 32
    next_num = mix(next_num, next_secret)
    next_num = prune(next_num)

    next_secret = next_num * 2048
    next_num = mix(next_num, next_secret)
    next_num = prune(next_num)
    return next_num

def mix(number: int, secret: int) -> int:

    xor = number ^ secret
    return xor

def prune(number: int) -> int:
    return number % 16777216