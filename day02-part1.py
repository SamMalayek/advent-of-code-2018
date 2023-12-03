from collections import Counter


def main():
    lines = open('day02.txt').read().splitlines()
    twoCounts = 0
    threeCounts = 0

    for line in lines:
        counter = Counter(line)
        curTwo = 0
        curThree = 0

        for key, val in counter.items():
            if val == 2:
                curTwo = 1
            elif val == 3:
                curThree = 1

        twoCounts += curTwo
        threeCounts += curThree

    print(twoCounts * threeCounts)


if __name__ == "__main__":
    main()
