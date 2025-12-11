import os
f = f"../inputs/{os.path.split(os.getcwd())[1]}.txt"

i = sorted([sum([int(c) for c in elf.split()]) for elf in open(f, "r").read().split("\n\n")], reverse=True)
print("p1", i[0])
print("p2", sum(i[:3]))
