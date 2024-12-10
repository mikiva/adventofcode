
import traceback
from collections import Counter
def test():
    ex = "2333133121414131402"
    #ex = "12345"

    run(ex)

def run(input: str):

    inp = iter(input)

    file = True
    disk = []
    file_id = 0
    while True:
        try:
            block = next(inp)
            if file:
                disk.extend([file_id for b in range(int(block))])
                file = False
                file_id += 1
            else:
                disk.extend(["." for b in range(int(block))])
                file = True
        except Exception as e:
            #print(traceback.format_exc())
            break


    disk2 = disk.copy()  
    #part1(disk)
    part2(disk2)



def part1(disk):
    head = 0
    tail = -1
    while True:

        head = disk.index(".")
        
        for idx in range(len(disk)-1, -1, -1):
            if disk[idx] != ".":
                tail = idx
                break

        if head > tail:
            break

        disk[head] = disk[tail]
        disk[tail] = "."
        
    checksum = 0
    for idx, block in enumerate(disk):
        if block == ".":
            continue
        checksum += (idx * int(block))

    print(disk)
    print(checksum)

def part2(disk):
    tail = len(disk) - 1

    moved = set()


    file_sizes = Counter(d for d in disk if d != ".")
    #file_sizes = Counter({k: v for k,v   in counter.items() if k != "."})
    file_ids = sorted(file_sizes)
    

    #return

    while True:

        if len(file_ids) == 0:
            break

        file_id = file_ids.pop()

        

        size_needed = file_sizes[file_id]

        #print(size_needed)
        before = len(moved)
        while True:
            head = disk.index(".")
            head_end = 0
            for idx in range(head, len(disk)):
                if disk[idx] != ".":
                    print("head end", idx,"head", head )
                    head_end = idx -1
                    break

            empty_size = head_end - head   
            print(file_id,head, head_end, empty_size, size_needed)

            if empty_size <= size_needed:
                
                for idx in range(head, head_end):
                    disk[idx] = file_id
                
                moved.add(file_id)
                continue
            if len(moved) > before:
                break



    print(moved)
    checksum = 0
    for idx, block in enumerate(disk):
        if block == ".":
            continue
        checksum += (idx * int(block))

    print(disk)
    print(checksum)