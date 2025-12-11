import os

f = f"../inputs/{os.path.split(os.getcwd())[1]}.txt"
operations = open(f).read().split("\n")


def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


cycle = 1
X = 1
signal = 0
cycles = []
for operation in operations:
    if operation == "noop":
        cycle += 1
        cycles.append(X)
        continue

    [_, count] = operation.split(" ")
    count = int(count)
    for c in range(2):
        cycles.append(X)
        if cycle == 20:
            signal += (X * cycle)

        elif ((cycle - 20) % 40) == 0:
            signal += (X * cycle)

        if c == 1:
            X += count

        cycle += 1

cycles = list(chunks(cycles, 40))

writing = []

for cy in cycles:
    line = []
    for i, cyc in enumerate(cy):
        if cyc is None:
            line.append(" . ")
            # print(".", end=" ")
        else:
            line.append("#" if (i - 1) <= cyc <= (i + 1) else ".")

    writing.append(line)
letters = "\n".join([" ".join(l) for l in writing])

print("p1", signal)
print("p2\n", letters)
print("==========")
