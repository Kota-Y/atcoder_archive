def main():
    n, a, b = map(int, input().split())

    if (b - a) % 2 == 0:
        ans = (b - a) // 2
    else:
        if a - 1 < n - b:
            ans = a - 1 + 1 + (b - a + 1 - 1) // 2
        else:
            ans = n - b + 1 + (n - a - n + b) // 2

    print(ans)

if __name__ == '__main__':
    main()