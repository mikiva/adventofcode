from collections import defaultdict
nums = [7, 14, 0, 17, 11, 1, 2]
#nums = [0,3,6]


def get_next_number(spoken, nums):
    last = nums[-1]
    if len(spoken[last]) > 1:
        num = len(nums) - spoken[last][-2]
    else:
        num = 0
    return num



def play(max_turns):

    spoken = defaultdict(list)


    for i, s in enumerate(nums):
        spoken[s].append(i+1)


    while 1 == 1:


        num = get_next_number(spoken, nums)
        nums.append(num)

        spoken[num].append(len(nums))
        if len(nums) == max_turns:
            return num
    return -1

def solve():
    print(f'A: {play(2020)}')
    print(f'B: {play(30000000)}')


if __name__ == "__main__":
    solve()
