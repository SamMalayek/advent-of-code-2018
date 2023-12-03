from collections import Counter


def main():
    lines = open('day02.txt').read().splitlines()
    twoCounts = 0
    threeCounts = 0

    for line in lines:
        counter = Counter(line)
        if 2 in counter.values():
            twoCounts += 1
        if 3 in counter.values():
            threeCounts += 1

    print(twoCounts * threeCounts)


if __name__ == "__main__":
    main()
