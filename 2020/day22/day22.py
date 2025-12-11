from copy import deepcopy
from collections import defaultdict, deque


def read_input(filename):
    p1, p2 = open(filename).read().split("\n\n")

    pd1, pd2 = [],[]

    for p in p1.split("\n"):
        if p.startswith("Player"):
            continue
        pd1.append(int(p))
    for p in p2.split("\n"):
        if p.startswith("Player"):
            continue
        pd2.append(int(p))

    return pd1, pd2

def play(p1, p2, part2=False):
    seen = set()
    while p1 and p2:
        seen_key = (tuple(p1), tuple(p2))
        if part2 and seen_key in seen:
            return True, p1

        seen.add((seen_key))

        p1card,p2card = p1.pop(0), p2.pop(0)

        if part2 and (len(p1) >= p1card and len(p2) >= p2card):
            new_p1card = p1[:p1card]
            new_p2card = p2[:p2card]
            p1_winner,_ = play(new_p1card, new_p2card, part2)
        else:
            p1_winner = p1card > p2card

        if p1_winner:
            p1.append(p1card)
            p1.append(p2card)
        else:
            p2.append(p2card)
            p2.append(p1card)


    return (True, p1) if p1 else (False, p2)

def play_game(p1, p2, part2=False):
    player, deck=play(p1, p2, part2)
    count=0
    for i, p in enumerate(deck):
        count += p * (len(deck) - i)
    return player, count


def solve(filename):
    p1, p2 = read_input(filename)

    winner, score = play_game(deepcopy(p1),deepcopy(p2))
    print(f'A: Winner player: {1 if winner else 2} - {score}')
    winner, score = play_game(deepcopy(p1),deepcopy(p2), True)
    print(f'B: Winner player: {1 if winner else 2} - {score}')


if __name__ == "__main__":
    solve("input")
