
def main():
    lines = open('day02.txt').read().splitlines()
    seen = set()

    for line in lines:
        for curSeen in seen:
            diffIndices = [i for i, (c1, c2) in enumerate(zip(line, curSeen)) if c1 != c2]

            if len(diffIndices) == 1:
                i = diffIndices[0]
                print(line[:i] + line[i + 1:])

        seen.add(line)


if __name__ == "__main__":
    main()
