def main():
    a, b, x = map(int, input().split())

    if a + b < x:
        print('NO')
        exit()

    if a > x:
        print('NO')
        exit()

    print('YES')


if __name__ == '__main__':
    main()