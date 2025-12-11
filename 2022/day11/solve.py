import os
import re
from functools import lru_cache

print("START==========")

f = f"../inputs/{os.path.split(os.getcwd())[1]}.txt"
#f = "../inputs/{}.txt".format(os.path.split(os.getcwd())[1])
notes = open(f).read().split("\n\n")

all_notes = [[n.strip() for n in note.split("\n")] for note in notes]


# print(*notes, sep="\n")

@lru_cache(maxsize=10000)
def evaluate(item, op, by):
    item = int(item)
    if by == "old":
        by = item


    if op == "*":
        return item * int(by)
    elif op == "+":
        return item + int(by)

@lru_cache(maxsize=10000)
def floor_div(item, by):
    return item // by


@lru_cache(maxsize=10000)
def check_divisibilty(item, by):
    return item % by == 0


def monkey_do(monkeys, m, worried=False):
   # print(m)
    for item in m["items"]:
        m["inspected"] += 1
        op, by = m["operation"]
        item = evaluate(item, op, by)
        if not worried:
            item = floor_div(item, 3)
        else:
            item = item % lcm


        test = m["test"]
        item = int(item)
        if check_divisibilty(item, test["divisible"]):
            monkeys[int(test["truthy"])]["items"].append(item)
        else:
            monkeys[int(test["falsy"])]["items"].append(item)
    m["items"] = []

lcm = 1
def monkeybusiness(rounds, worried=False):
    global lcm
    monkeys = []
    for key, note in enumerate(all_notes):
        monkey = {}
        m_id = int(note[0][-2])
        monkey["id"] = m_id

        items = re.findall("\d+", note[1])
        monkey["items"] = [int(i) for i in items]

        operation = note[2].split()[-2:]
        monkey["operation"] = operation

        monkey["test"] = dict(divisible=int(note[3].split()[-1]), truthy=int(note[4].split()[-1]),
                              falsy=int(note[5].split()[-1]))
        monkey["inspected"] = 0
        monkeys.append(monkey)
        lcm *= int(note[3].split()[-1])

    for _ in range(rounds):
        for monkey in monkeys:
            monkey_do(monkeys, monkey, worried=worried)

    most_active = sorted(monkeys, key=lambda k: k["inspected"], reverse=True)
    return most_active[0]["inspected"] * most_active[1]["inspected"]


#
#
# print("before")
# print(*[monkey["items"] for monkey in monkeys], sep="\n")
#
# for _ in range(10_000):
#     for monkey in monkeys2:
#         #items = monkey["items"]
#         monkey_do(monkey)


# print("after")
#
##print(*[monkey["items"] for monkey in monkeys], sep="\n")
# print("m1")
# print(*monkeys, sep="\n")
# print("m2")
#print(*monkeys2, sep="\n")
#

print("p1", monkeybusiness(20))
print("p2", monkeybusiness(10000, True))

print("==========")
