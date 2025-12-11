import os

f = f"../inputs/{os.path.split(os.getcwd())[1]}.txt"

lines = [l.split(",") for l in open(f).read().split("\n")]

pairs = []
overlaps = []
for line in lines:
    p1, p2 = line
    p1 = tuple(int(i) for i in p1.split("-"))
    p2 = tuple(int(i) for i in p2.split("-"))
    s1 = {s for s in range(p1[0], p1[-1] + 1)}
    s2 = {s for s in range(p2[0], p2[-1] + 1)}

    sub1 = s1.issubset(s2)
    sub2 = s2.issubset(s1)

    if sub1 or sub2:
        pairs.append((s1, s2))

    if s1.intersection(s2):
        overlaps.append((s1, s2))

print("==in==")
print("p1", len(pairs))
print("p2", len(overlaps))
print("==out==")
