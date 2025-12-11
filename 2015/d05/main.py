import re
data_input = []

with open("in", "r") as file:
    data_input = file.read().split("\n")

vowels = "aeiou"
forbidden =["ab", "cd", "pq", "xy"]

def check_forbidden(to_check):

    for forbid in forbidden:
        if forbid in to_check:
            return True


    return False

def check_vowels(to_check):
    stripped = []
    for letter in to_check:
        if letter in vowels:
            stripped.append(letter)
    return len(stripped) >= 3

def check_double_letters(to_check):
    previous = to_check[0]
    for letter in to_check[1:]:
        if letter == previous:
            return True
        previous = letter


def check_letter_between(string):
    previous = string[0]
    idx = 0
    for letter in string[2:]:
        if previous == letter:
            return True
        idx += 1
        previous = string[idx]

def check_pairs(string):
    for idx in range(len(string)-1):
        check = string[idx] + string[idx+1]
        if len(re.findall(check, string)) >=2:
            return True


def p2():

    nice = []
    for string in data_input:
        is_nice = True
        if not check_letter_between(string):
            is_nice = False

        if not check_pairs(string):
            is_nice = False




        if is_nice:
            nice.append(string)

    print("p2", len(nice))

def p1():
    nice = []
    for string in data_input:
        if check_forbidden(string) or not check_vowels(string) or not check_double_letters(string):
            continue            
        
        nice.append(string)


    print("p1", len(nice))


p1()
p2()