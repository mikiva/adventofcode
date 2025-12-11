import functools
import os
import re
import sys
from functools import lru_cache

print("START==========")


# print(*pairs, sep="\n")

def compare(a: list, b: list):
    try:
        for i in range(len(a)):
            left = a[i]
            right = b[i]
            if isinstance(left, int) and isinstance(right, int):
                if left < right:
                    return True
                elif left > right:
                    return False
                else:
                    continue
            elif isinstance(left, list) and isinstance(right, int):
                if compare(left, [right]) is None:
                    continue
                else:
                    return compare(left, [right])

            elif isinstance(left, int) and isinstance(right, list):
                if compare([left], right) is None:
                    continue
                else:
                    return compare([left], right)

            else:
                if compare(left, right) is None:
                    continue
                else:
                    return compare(left, right)
        if len(a) < len(b):
            return True

        return None

    except IndexError:
        return False


#STOLEN
def ordering(packets):
    for k in range(1, len(packets)):
        cur = packets[k]
        j = k
        while j > 0 and compare(cur, packets[j - 1]):
            packets[j] = packets[j - 1]
            j -= 1
            packets[j] = cur
    return packets

def solve(sort=False):
    f = f"../inputs/{os.path.split(os.getcwd())[1]}"

    if not sort:
        pairs = [pair.split("\n") for pair in open(f).read().split("\n\n")]
        pairs = [(eval(pair[0]), eval(pair[1])) for pair in pairs]
        correct = []
        for i, (p1, p2) in enumerate(pairs):
            if compare(p1, p2):
                correct.append(i + 1)

        return sum(correct)

    packets = [eval(pair) for pair in open(f).read().split("\n") if pair != ""]
    packets.append([[2]])
    packets.append([[6]])
    packets = ordering(packets)

    packets = [str(p) for p in packets]
    first = packets.index("[[2]]") +1
    second = packets.index("[[6]]") +1

    return first*second



print("p1", solve())
print("p2", solve(True))


print("=================")
