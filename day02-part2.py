
def main():
    lines = open('day02.txt').read().splitlines()
    seen = set()

    for line in lines:
        for curSeen in seen:
            if len(line) != len(curSeen):
                continue

            diff = 0
            indexDiff = -1

            for i in range(len(line)):
                if curSeen[i] != line[i]:
                    diff += 1
                    indexDiff = i
                if diff > 1:
                    break

            if diff == 1:
                print(line[0:indexDiff] + line[indexDiff + 1:len(line)])
                quit()

        seen.add(line)


if __name__ == "__main__":
    main()
