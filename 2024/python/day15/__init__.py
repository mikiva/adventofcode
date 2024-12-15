
from collections import namedtuple
def test():
    ex = """##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^"""

    ex2 = """########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

<^^>>>vv<v>>v<<"""

    run(ex)

def run(input: str):
    warehouse, movements = input.split("\n\n")
    warehouse = [[c for c in row] for row in warehouse.split("\n")]
    movements = [m for m in "".join(movements.split("\n"))]

    part1(warehouse, movements)


def part1(warehouse, movements):
    for y, row in enumerate(warehouse):
        for x, col in enumerate(row):
            if col == "@":
                position = [x,y]
    for direction in movements:
        if can_move(warehouse, position, direction):
            position = move(warehouse, position, direction)
        
    coordinates = 0
    for y, row in enumerate(warehouse):
        for x, col in enumerate(row):
            if col == "O":
                coordinates += 100 * y + x

    print("1: ", coordinates)


def move(warehouse, position, direction, actor="@"):
    x,y = position
    if direction in ["<", ">"]:
        new_pos = [x+1,y] if direction == ">" else [x-1,y]
        xx,yy = new_pos
        if warehouse[yy][xx] == "O":
            if can_move(warehouse, new_pos, direction, actor="O"):
                move(warehouse, new_pos, direction, actor="O")
    else:
        
        new_pos = [x, y+1] if direction == "v" else [x,y-1]
        
        xx,yy = new_pos
        if warehouse[yy][xx] == "O":
            if can_move(warehouse, new_pos, direction, actor="O"):
                move(warehouse, new_pos, direction, actor="O")

    nx,ny = new_pos
    warehouse[y][x] = "."
    warehouse[ny][nx] = actor
    return new_pos


def can_move(warehouse, position, direction, actor="@"):
    x,y = position
    check_location = actor
    match direction:
        case "<":
            while check_location != "#":
                x -= 1
                check_location = warehouse[y][x]
                
                if check_location == ".":
                    return True

        case "^":
            while check_location != "#":
                y -= 1
                check_location = warehouse[y][x]
                
                if check_location == ".":
                    return True
        case ">":
            while check_location != "#":
                x += 1
                check_location = warehouse[y][x]
                
                if check_location == ".":
                    return True
        case "v":
            while check_location != "#":
                y += 1
                check_location = warehouse[y][x]
                
                if check_location == ".":
                    return True

    return False



def print_warehouse(warehouse):
    for r in warehouse:
        for c in r:
            print(c, end="")
        print()