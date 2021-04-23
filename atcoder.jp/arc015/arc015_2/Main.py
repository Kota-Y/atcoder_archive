def main():
    n = int(input())

    ans1 = 0
    ans2 = 0
    ans3 = 0
    ans4 = 0
    ans5 = 0
    ans6 = 0

    for _ in range(n):
        a, b = map(float, input().split())
        if a >= 35:
            ans1 += 1
        if 35 > a >= 30:
            ans2 += 1
        if 30 > a >= 25:
            ans3 += 1
        if b >= 25:
            ans4 += 1
        if a >= 0 and b < 0:
            ans5 += 1
        if a < 0:
            ans6 += 1

    print(ans1, ans2, ans3, ans4, ans5, ans6)

if __name__ == '__main__':
    main()
