import re
from collections import defaultdict
import copy

from time import sleep

class Robot:
    position: tuple
    velocity: tuple
    def __init__(self, pos, vel):
        self.position = pos
        self.velocity = vel

    
    def walk(self, width: int, height: int, seconds=1):
        
        px, py = self.position
        vx, vy = self.velocity

        new_position = ((px+(vx * seconds))%width, (py+(vy*seconds))%height)

        self.position = new_position


    def get_quadrant(self, width, height):
        mx = width // 2
        my = height // 2


def test():
    ex = """p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3"""

    ex2 = "p=2,4 v=2,-3"

    run(ex, 11,7)

def run(input: str, width=101, height=103):
    #print(input)
    robots: list[Robot] = []
    for rob in input.split("\n"):
        locs = re.findall("(-?\d+,-?\d+)", rob)
        #print(locs)
        #for loc in locs:
        position = tuple(int(l) for l in locs[0].split(","))
        velocity = tuple(int(l) for l in locs[1].split(","))
        #print(position, velocity)
        robots.append(Robot(position, velocity))

    part1(copy.deepcopy(robots), width, height)
    part2(copy.deepcopy(robots), width, height)

def walk_robots(robots,width, height, seconds=1):
    for r in robots:
        r.walk(width, height, seconds)


def part2(robots, width, height):
    seconds = 0
    while True:
        seconds += 1
        walk_robots(robots, width, height)
        positions = defaultdict(int)
        for robot in robots:
            positions[robot.position] += 1
        
        for (x,y) in positions.keys():
            if all((x, y+i) in positions and (x+i, y) in positions for i in range(20)):
                #print_grid(robots, width, height, include_center=True)
                print("2: ", seconds)
                return
            

def part1(robots, width, height):
    robots = robots[:]
    for r in robots:
        r.walk(width, height, 100)

    #print_grid(robots, width, height)

    quads = defaultdict(int)
    for robot in robots:
        x,y = robot.position
        if x < width // 2:
            if y < height // 2:
                quads[1] += 1
            elif y > height // 2:
                quads[2] += 1
        elif x > width // 2:
            if y < height // 2:
                quads[3] += 1
            elif y > height // 2:
                quads[4] += 1

    safety = 1
    for quad in list(quads.values()):
        safety *= quad
    print("1: ", safety)


def print_grid(robots, width, height, include_center=False):
    positions = defaultdict(int)
    for robot in robots:
        positions[robot.position] += 1
    for y in range(height):
        for x in range(width):
            if x == width //2 or y == height//2:
                print(" " if not include_center else (positions[(x,y)] if positions[(x,y)] > 0 else "."), end="")
            elif (x,y) in positions:
                print(positions[(x,y)], end="")
            else:
                print(".", end="")
        print()