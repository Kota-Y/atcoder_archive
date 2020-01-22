def main():
    n,x = map(int, input().split())
    num_list = list(map(int, input().split()))

    sum = 0
    ans = 1

    for i in num_list:
        sum += i
        if sum <= x:
            ans += 1

    print(ans)

if __name__ == '__main__':
    main()