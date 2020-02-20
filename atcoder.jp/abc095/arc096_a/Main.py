def main():
    a, b, c, x, y = map(int, input().split())

    ans = 1000000000

    tmp_x = x
    tmp_y = y

    for ab in range(max(x, y)+1):
        x -= ab
        y -= ab
        if x < 0:
            x = 0
        if y < 0:
            y = 0
        ans = min(ans, a * x + b * y + 2 * ab * c)
        x, y = tmp_x, tmp_y

    print(ans)

if __name__ == '__main__':
    main()