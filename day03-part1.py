import re


def main():
    lines = open('day03.txt').read().splitlines()

    grid = [[0 for _ in range(1000)] for _ in range(1000)]
    resp = 0

    for line in lines:
        num, col, row, colLen, rowLen = [int(a) for a in re.split('[^0-9]', line) if a]

        for curRow in range(row, row+rowLen):
            for curCol in range(col, col+colLen):
                if grid[curRow][curCol] != 0:
                    if grid[curRow][curCol] != 'X':
                        resp += 1
                    grid[curRow][curCol] = 'X'
                else:
                    grid[curRow][curCol] = num

    print(resp)


if __name__ == "__main__":
    main()
