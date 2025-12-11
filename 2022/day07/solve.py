import os
import sys
from collections import defaultdict

f = f"../inputs/{os.path.split(os.getcwd())[1]}.txt"
lines = open(f).read().split("\n")
dirs = defaultdict(list)
cwd = ""
for line in lines:
    match line.split(" "):
        case ["$", "cd", directory] if directory.startswith("/"):
            cwd = directory
        case ["$", "cd", directory] if directory == "..":
            cwd = "/".join(cwd.split("/")[:-1])
            if len(cwd) == 0: cwd = "/"
        case ["$", "cd", directory]:
            cwd += directory if cwd.endswith("/") else "/" + directory
        case [size, file_name] if size.isdigit():
            dirs[cwd].append(int(size))
            for k in [key for key in dirs.keys() if key != cwd and key in cwd]:
                dirs[k].append(int(size))

    if cwd not in dirs.keys():
        dirs[cwd] = list()

sizes = 0
for dir, s in dirs.items():
    sub = sum(s)
    if sub <= 100_000:
        sizes += sub

total_disk_space = 70_000_000
unused_needed = 30_000_000
current_unused = total_disk_space - sum(dirs["/"])
delete_needed = unused_needed - current_unused
cur = sys.maxsize
to_delete = {}
for d, content in dirs.items():
    size = sum(content)
    if size > delete_needed:
        to_delete[d] = size

print("p1", sizes, sizes == 1315285)
mini_to_delete = min(to_delete.values())
print("p2", mini_to_delete, mini_to_delete == 9847279)
