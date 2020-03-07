def main():
    n, a, b = map(int, input().split())

    if a == 0:
        print(0)
        exit()
    if b == 0:
        print(n)
        exit()

    tmp = n % ( a + b )

    if tmp >= a:
        tmp = a

    print(n // (a+b) * a + tmp)

if __name__ == '__main__':
    main()