
from collections import defaultdict
from math import ceil

def test():
    ex = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""

    run(ex)

def run(input):

    [rules, page_numbers] = input.split("\n\n")
    rule_set = defaultdict(list)
    rules = [ rule_set[int(r[0])].append(int(r[1])) for r in [rule.split("|") for rule in rules.split("\n")]]

    page_numbers = [[int(s) for s in q] for  q in [p for p in [page.split(",") for page in page_numbers.split("\n")]]]

    do(rule_set, page_numbers)


def check_agains_rules(rules, update):
    is_correct = True
    for i, page in enumerate(update):
        if page in rules:
            to_check = update[i+1:]
            to_check_rev = update[:i]
            for u in to_check:
                if u not in rules[page]:
                    is_correct = False
            for u in to_check_rev:
                if u in rules[page]:
                    is_correct = False

            if not is_correct:
                break
    return is_correct


def get_center_page(update):
    middle_idx = ceil((len(update) -1) / 2)
    middle_page = update[middle_idx]
    return middle_page




def fix_update(rules, update):

    rules_list = dict()
    for page in update:
        rules_list[page] = len([r for r in rules[page] if r in update])

    sorted_pages = dict()
    for key in sorted(rules_list, key=rules_list.get, reverse=True):
        sorted_pages[key] = rules_list[key]

    return get_center_page(list(sorted_pages.keys()))

def do(rules, updates):
    middle = 0
    incorrect_updates = []
    for update in updates:
        if check_agains_rules(rules, update):
            middle += get_center_page(update)
        else:
            incorrect_updates.append(update)
    middle_fixed = 0
    for update in incorrect_updates:
        middle_fixed += fix_update(rules, update)


    print("1: ", middle)
    print("2: ", middle_fixed)

