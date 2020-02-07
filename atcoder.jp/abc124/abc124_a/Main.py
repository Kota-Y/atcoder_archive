def main():
    a, b = map(int, input().split())

    ans = 0

    if a == b:
        ans = a * 2
    else:
        ans = max(a,b) * 2 - 1

    print(ans)

if __name__ == '__main__':
    main()