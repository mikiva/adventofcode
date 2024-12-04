
from pprint import pprint


def test():
    ex = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""

    run(ex)

def check_horizontal(r, c, matrix):
    if c+3 < len(matrix[r]):
        word = ""
        for x in range(4):
            word += matrix[r][c+x]
        reversed = word[::-1]
        if "XMAS" in [word, reversed]:
            return True

def check_vertical(r,c, matrix):
    if r+3 < len(matrix):
        word = ""
        for x in range(4):
            try:
                word += matrix[r+x][c]
            except:
                print(word, len(matrix) , matrix[r+x-1], r+x)
                
        reversed = word[::-1]
        if "XMAS" in [word, reversed]:
            return True
    

def check_diagonal_right(r,c,matrix, check="XMAS"):
    width = len(check)
    if r+width-1 < len(matrix) and c+width-1 < len(matrix[r]):
        word = ""
        for l in range(width):
            word += matrix[r+l][c+l]
        reversed = word[::-1]
        if check in [word, reversed]:
            return True
    ...
def check_diagonal_left(r,c,matrix, check="XMAS"):
    width = len(check)
    if r+width-1 < len(matrix) and c-width-1 >= 0:
        word = ""
        for l in range(width):
            word += matrix[r+l][c-l]
        reversed = word[::-1]
        if check in [word, reversed]:
            return True
    ...


def part1(rows: list):
    found = 0

    for rdx, row in enumerate(rows):
        for cdx, _ in enumerate(row):
            if check_horizontal(rdx, cdx, rows):
                found += 1
            if check_vertical(rdx, cdx, rows):
                found += 1
            if check_diagonal_right(rdx, cdx, rows):
                found += 1
            if check_diagonal_left(rdx, cdx, rows):
                found += 1

    return found


def part2(rows):
    found = 0
    for rdx, row in enumerate(rows):
        for cdx in range(len(row)):

            if check_diagonal_right(rdx, cdx, rows, "MAS"):
                if check_diagonal_left(rdx, cdx +2, rows, "MAS"):
                    found += 1
    return found


def run(input):
    rows = list(list(l) for l in input.split("\n"))
    print("1: ", part1(rows))
    print("2: ", part2(rows))
