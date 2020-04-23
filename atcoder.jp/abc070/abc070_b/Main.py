def main():
    a, b, c, d = map(int, input().split())

    if a <= c:
        if b <= c:
            ans = 0
        elif b <= d:
            ans = b - c
        else:
            ans = d - c
    else:
        if d <= a:
            ans = 0
        elif d <= b:
            ans = d - a
        else:
            ans = b - a


    print(ans)

if __name__ == '__main__':
    main()