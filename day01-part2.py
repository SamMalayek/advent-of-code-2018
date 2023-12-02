
def main():
    lines = open('day01.txt').read().splitlines()
    seen = {0}
    resp = 0

    while True:
        for line in lines:
            resp += eval(line)
            if resp in seen:
                print(resp)
                quit()
            seen.add(resp)


if __name__ == "__main__":
    main()
