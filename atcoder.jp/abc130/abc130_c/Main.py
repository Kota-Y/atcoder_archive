def main():
    w, h, x, y = map(int, input().split())


    ans = w * h / 2
    hasDivision = 1 if x + x == w and y + y == h else 0

    print(ans, hasDivision)

if __name__ == '__main__':
    main()