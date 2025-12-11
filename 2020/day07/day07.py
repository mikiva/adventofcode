
import re

bagexp = "(([a-z]+) ([a-z]+))(?=\sbag|bags)"
color_pattern = re.compile(bagexp)

color_regexp = "(\w+ \w+) bags contain"
col_pat = re.compile(color_regexp)
content_regexp = "(?:(\d+) (\w+ \w+))"
cont_pat = re.compile(content_regexp)

bags = dict()
rules = [] 
with open("input.txt", "r") as inp:
    rules = inp.read().split("\n")
    for rule in rules:
        color = col_pat.match(rule)[1]
        contains = re.findall(cont_pat,rule)
        bags[color] = set()
        for c in contains:
            bags[color].add(tuple((c[1] , int(c[0]))))
        


def a():
    colors = set()
    pre, cur = -1 , 0
    while(cur != pre):
        pre = cur
        for rule in rules:
            color = col_pat.match(rule)[1]
            if "shiny gold" in rule and not rule.startswith("shiny gold"):
                colors.add(color)
            for s in [x[0] for x in re.findall(bagexp, rule)]:
                if s in colors:
                    colors.add(color)

        cur = len(colors)
    return len(colors)


def count_bags(bagIn, arr):
    bag = bags[bagIn]
    if len(bag) == 0:
        arr.append(bag)
    else:
        for b in bag:
            for cc in range(b[1]):
                count_bags(b[0], arr)
        arr.append(b)
    return arr

print("a", a())
print("b", (len(count_bags("shiny gold", [] )) -1 ))
