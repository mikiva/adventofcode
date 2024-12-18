def test():
    ex = """5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0"""

    run(ex, 7, 12)

visited = set()
def run(input: str, size=71, bytes=1024):

    points = []
    for pos in input.split("\n"):
        x,y = pos.split(",")
        points.append((int(x), int(y)))


    grid = [["." for _ in range(size)] for _ in range(size)]
    
    for x,y in points[:bytes]:
        grid[y][x] = "#"

    steps = count_steps(grid) 
    print("1: ", steps)

    # PART 2
    count = 1
    last_byte = ()
    while True:
        found_steps = count_steps(grid) 
        if found_steps == 0:
            break
        for x,y in points[:bytes+count]:
            grid[y][x] = "#"
            last_byte = (x,y)
        count += 1


    print("2: ", ",".join(map(str,last_byte)))

   
def count_steps(grid):
    start = (0,0)
    ending = (len(grid)-1, len(grid)-1)
    steps = 0
    size = len(grid)

    queue = []
    queue.append(start)
    visited = set([start])
    path_from = {}
    found = False
    while queue:
        path = queue.pop(0)
        x,y = path
        if (x,y) == ending:
            found = True
            break
        
        # UP
        if x > 0 and x < size and grid[y][x-1] == "." and (x-1, y) not in visited:
            queue.append((x-1, y))
            visited.add((x-1,y))
            path_from[(x-1, y)] = (x,y)
        # DOWN
        if x < size - 1 and grid[y][x+1] == "." and (x+1, y) not in visited:
            queue.append((x+1, y))
            visited.add((x+1,y))
            path_from[(x+1, y)] = (x,y)
        
        # RIGHT
        if y < size -1 and grid[y+1][x] == "." and (x, y+1) not in visited:
            queue.append((x, y+1))
            visited.add((x,y+1))
            path_from[(x, y+1)] = (x,y)
        # LEFT
        if y > 0 and grid[y-1][x] == "." and (x, y-1) not in visited:
            queue.append((x, y-1))
            visited.add((x,y-1))
            path_from[(x, y-1)] = (x,y)


    position = ending
    steps = []
    if found:
        while position != start:
            position = path_from[position]
            steps.append(position)
    return len(steps)