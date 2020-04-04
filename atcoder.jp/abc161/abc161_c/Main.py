def main():
    n, k = map(int, input().split())

    if n == 0:
        print(0)
        exit()

    if k == 1:
        print(0)
        exit()

    if n == k:
        print(0)
        exit()

    dist = abs(n-k)

    if n < dist:
        print(n)
        exit()

    if n == dist:
        print(0)
        exit()
                
    print(abs((n // k + 1) * k - n))
    exit()


if __name__ == '__main__':
    main()