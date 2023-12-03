import re


def main():
    lines = open('day03.txt').read().splitlines()

    grid = [[0 for _ in range(1000)] for _ in range(1000)]
    claims = set()

    for line in lines:
        num, col, row, colLen, rowLen = [int(a) for a in re.split('[^0-9]', line) if a]
        claims.add(num)
        for curRow in range(row, row+rowLen):
            for curCol in range(col, col+colLen):
                if grid[curRow][curCol] != 0:
                    claims.discard(grid[curRow][curCol])
                    claims.discard(num)
                    grid[curRow][curCol] = 'X'
                else:
                    grid[curRow][curCol] = num

    print(next(iter(claims)))


if __name__ == "__main__":
    main()
