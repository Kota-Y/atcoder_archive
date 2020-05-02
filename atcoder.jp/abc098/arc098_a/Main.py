def main():
    n = int(input())
    s = input()

    all_east = 0
    all_west = 0

    for i in range(n):
        if s[i] == 'W':
            all_west += 1
        else:
            all_east += 1

    count = 10 ** 6

    now_west = 0
    for i in range(n):
        if s[i] == 'E':
            all_east -= 1
        count = min(count, all_east + now_west)
        if s[i] == 'W':
            now_west += 1

    print(count)

if __name__ == '__main__':
    main()