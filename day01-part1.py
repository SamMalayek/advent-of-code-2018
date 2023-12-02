
def main():
    lines = open('day01.txt').read().splitlines()

    resp = 0
    for line in lines:
        resp += eval(line)

    print(resp)


if __name__ == "__main__":
    main()
