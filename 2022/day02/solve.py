import os

f = f"../inputs/{os.path.split(os.getcwd())[1]}.txt"


def play(a, b) -> int:
    a, b = "ABC".index(a), "XYZ".index(b)
    score, outcome = b + 1, (b - a) % 3
    if outcome == 0:
        return 3 + score
    elif outcome == 1:
        return 6 + score
    else:
        return 0 + score


def play_mod(a, b) -> int:
    s = "ABC".index(a)

    if b == "X":
        return (s - 1) % 3 + 1
    elif b == "Y":
        return 3 + s + 1
    else:
        return 6 + (s + 1) % 3 + 1


i = [g.strip() for g in open(f).readlines()]
s1, s2 = 0, 0
for game in i:
    a, b = game.split()
    p1 = play(a, b)
    s1 += p1

    p2 = play_mod(a, b)
    s2 += p2

print("p1", s1)
print("p2", s2)
