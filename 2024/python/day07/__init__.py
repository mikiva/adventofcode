
from itertools import product
from collections import defaultdict

def test():
    ex = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""

    run(ex)


equations = dict()

def run(input):
    lines = [r for r in [inp for inp in input.split("\n")]]
    for line in lines:
        [goal, nums] = line.split(": ")
        numbers =[int(s) for s in  nums.split(" ")]
        equations[int(goal)] = numbers

    correct_1 = 0
    correct_2 = 0
    for (goal, equation) in equations.items():
        if is_correct(goal, equation, "+*"):
            correct_1 += goal
        if is_correct(goal, equation, "+*|"):
            correct_2 += goal
    
    print("1: ", correct_1)
    print("2: ", correct_2)


def is_correct(goal, numbers, operations):

    bits = len(numbers) - 1
    operators_list = product(operations, repeat=bits)
    for operators in operators_list:
        current = numbers[0]
        for i, op in enumerate(operators):
            if op == "+":
                current += numbers[i+1]
            elif op == "*":
                current *= numbers[i+1]
            elif op == "|":
                current = int(str(current) + str(numbers[i+1]))


            if current > goal:
                break
        if current == goal:
            return True

    return False

