def main():
    n = int(input())
    num_list = list(map(int, input().split()))

    ans = 1

    tmp = num_list[0]

    for i in range(1,n):
        if tmp <= num_list[i]:
            ans += 1
            tmp = num_list[i]

    print(ans)

if __name__ == '__main__':
    main()