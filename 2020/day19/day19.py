import re

part2 = False
rules = dict()

def read_input(file):
    global rules
    rules_raw, messages = open(file).read().split("\n\n")

    mess = []
    rule_list = dict()

    for rule in rules_raw.split("\n"):
        id, content = rule.split(":")
        rule_list[id] = content.strip().split()
    for message in messages.split("\n"):
        mess.append(message)

    rules = rule_list
    return mess


def get_regex_part(part):
    if part.startswith('"'):
        return part[1]
    elif part == '|':
        return '|'
    else: 
        r = build_regexp(part)
        if len(r) == 1: return r
        return '(' + r + ')'

def build_regexp(number):

    if part2:
         if number == '8':
             return '(' + build_regexp("42") + ')+'
         elif number == '11':
             r = '|'.join(get_regex_part('42')*n + get_regex_part('31')*n for n in range(1,6))
             return r

    return ''.join(get_regex_part(reg) for reg in rules[number])


def run(messages):

    regexp = build_regexp('0')
    count = 0
    for message in messages:
        if re.match('^' + regexp + '$', message):
            count += 1
    return count

def solve(file):
    global part2
    messages = read_input(file)
    print(f'A: {run(messages)}')

    part2 = True
    print(f'B: {run(messages)}')

if __name__ == "__main__":
    solve("input")