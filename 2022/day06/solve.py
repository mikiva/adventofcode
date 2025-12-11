import os

f = f"../inputs/{os.path.split(os.getcwd())[1]}.txt"
chars = [f for f in open(f).read()]


def find_marker(w):
    for i, c in enumerate(chars):
        if len(set(chars[i:i + w])) == w:
            return i + w


print(find_marker(4))
print(find_marker(14))
