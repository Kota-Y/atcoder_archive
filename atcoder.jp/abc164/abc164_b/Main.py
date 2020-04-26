def main():
    a, b, c, d = map(int, input().split())

    for i in range(10000):
        if c <= 0:
            print('Yes')
            exit()
        if a <= 0:
            print('No')
            exit()
        if i % 2 == 0:
            c -= b
        else:
            a -= d

if __name__ == '__main__':
    main()