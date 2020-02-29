def main():
    n, m = map(int, input().split())

    tmp = 5 if m > 5 else m

    print(1900 * m * 2 ** tmp + 100 * (n-m) * 2 ** tmp)

if __name__ == '__main__':
    main()